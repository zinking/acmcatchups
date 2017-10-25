public abstract class AbstractQueuedSynchronizer extends AbstractOwnableSynchronizer implements java.io.serializable {
    private static final long serialVersionUID = 777777777;

    protected AbstractQueuedSynchronizer() {}

    static final class Node {
        static final Node SHARED = new Node();
        static final Node EXCLUSIVE = null;
        static final int CANCELLED = 1;
        static final int SIGNAL = -1;
        static final int CONDITION = -2;
        static final int PROPAGATE = -3;
        volatile int waitStatus;
        volatile Node prev;
        volatile Node next;
        volatile Thread thread;
        Node nextWaiter; //TO UNDERSTAND MORE
        final boolean isShared() { return nextWaiter == SHARED; }
        final Node predecessor() throws NullPointerException {
            Node p = prev;
            if (p == null) throw new NullPointerException;
            else return p;
        }
        Node() {}
        Node(Thread thread, Node mode) {
            this.nextWater = mode;
            this.thread = thread;
        }
        Node(Thread thread, int waitStatus) {
            this.waitStatus = waitStatus;
            this.thread = thread;
        }
    }

    private transient volatile Node head;
    private transient volatile Node tail;
    private volatile int state;
    protected final int getState() { return state; }
    protected void setState(int newState) { state = newState; }
    protected final boolean compareAndSetState(int expect, int update) {
        return unsafe.compareAndSwapInt(this, stateOffset, expect, update);
    }
    static final long spinForTimeoutThreshold = 1000L;
    private Node enq(final Node node) {
        for(;;) {
            Node t = tail;
            if (t == null) {
                if (compareAndSetHead(new Node())) tail = head
            }
            else {
                node.prev = t;
                if (compareAndSetTail(t,node)) {
                    t.next = node;
                    return t;
                }
            }
        }
    }
    private Node addWaiter(Node mode) {
        Node node = new Node(Thread.currentThread(), mode);
        Node pred = tail;
        if (pred != null) { //this seems exactly the same as enq???
            node.prev = pred;
            if (compareAndSetTail(pred, node)) {
                pred.next = node;
                return node;
            }
        }
        enq(node); //why not directly use enq? (tail null/nonNull case all seems overlap???)
        return node;
    }
    private void setHead(Node node) {
        head = node;
        node.thread = null;
        node.prev = null;
    }
    private void unparkSuccessor(Node node) {
        int ws = node.waitStatus; //if status is negative(need signal) clear its anticipation
        if (ws < 0) compareAndSetWaitStatus(node, ws, 0);
        Node s = node.next;
        // thread to unpark is held in its successor, which is normally just the next node.
        // but if cancelled or apparently null, traverse backwards from tail to find the actual 
        if (s == null || s.waitStatus > 0) {
            s = null;
            for (Node t = tail; t != null && t != node; t = t.prev)
                if (t.waitStatus <= 0) s = t;
        }
        if (s != null) LockSupport.unpark(s.thread);
    }
    private void doReleaseShared() { //don't understand , what is the shared propogate in earth ???
        for (;;) {
            Node h = head;
            if (h != null && h != tail) {
                int ws = h.waitStatus;
                if (ws == Node.SIGNAL) {
                    if (!compareAndSetWaitStatus(h, Node.SIGNAL, 0)) continue;
                    unparkSuccessor(h);
                }
                else if (ws == 0 && !compareAndSetWaitStatus(h, 0, Node.PROPAGATE)) continue;
            }
            if (h == head) break;
        }
    }
    private void setHeadAndPropagate(Node node, int propagate) { //TODO``
        Node h = head;
        setHead(node);
        if (propagate > 0 || h == null || h.waitStatus < 0 || (h = head) == null || h.waitStatus < 0) {
            Node s = node.next;
            if (s == null || s.isShared()) doReleaseShared();
        }
    }
    private void cancelAcquire(Node node) {
        if (node == null) return;
        node.thread = null;
        Node pred = node.prev;
        while (pred.waitStatus > 0) node.prev = pred = pred.prev; //skip cancelled predecessors
        Node predNext = pred.next;
        node.waitStatus = Node.CANCELLED; //can use unconditional write, why ?
        if (node == tail && compareAndSetTail(node, pred)) {
            compareAndSetNext(pred, predNext, null);
        } else {
            int ws;
            if (pred != head &&
                ((ws = pred.waitStatus) == Node.SIGNAL ||
                 (ws <= 0 && compareAndSetWaitStatus(pred, ws, Node.SIGNAL))) &&
                pred.thread != null) {
                Node next = node.next;
                if (next != null && next.waitStatus <= 0) compareAndSetNext(pred,predNext, next);
            }
            else {
                unparkSuccessor(node);
            }
            node.next = node; //help gc, does this really help gc???
        }
    }
    // checks and updates the status for a node that failed to acquire
    // returns true if the thread should block, this is the main signal control
    private static boolean shouldParkAfterFailedAcquire(Node pred, Node node) {
        int ws = pred.waitStatus;
        if (ws == Node.SIGNAL) return true;
        if (ws > 0) {
            do {
                node.prev = pred = pred.prev;
            } while (pred.waitStatus > 0);
            pred.next = node;
        }
        else {
            compareAndSetWaitStatus(pred, ws, node.SIGNAL);
        }
        return false;
    }
    static void selfInterrupt() {
        Thread.currentThread().interrupt();
    }
    private final boolean parkAndCheckInterrupt() {
        LockSupport.park(this);
        return Thread.interrupted();
    }
    final boolean acquireQueued(final Node node, int arg) {
        boolean failed = true;
        try {
            boolean interrupted = false;
            for (;;) {
                final Node p = node.predecessor();
                if (p == head && tryAcquire(arg)) {
                    setHead(node);
                    p.next = null;
                    failed = false;
                    return interrupted;
                }
                if (shouldParkAfterFailedAcquire(p, node) && parkAndCheckInterrupt())
                    interrupted = true;
            }
        } finally {
            if (failed) cancelAcquire(node);
        }
    }
    private void doAcquireInterruptibly(int arg) throws InterruptedException {
        final Node node = addWaiter(node.EXCLUSIVE);
        boolean failed = true;
        try {
            for (;;) {
                final Node p = node.predecessor();
                if (p == head && tryAcquire(arg)) {
                    setHead(node);
                    p.next = null;
                    failed = false;
                    return;
                }
                if (shouldParkAfterFailedAcquire(p, node) && parkAndCheckInterrupt())
                    throw new InterruptedException();
            }
        }
        finally {
            if (failed) cancelAcquire(node);
        }
    }
    private boolean doAcquireNanos(int arg, long nanosTimeout) throws InterruptedException {
        if (nanosTimeout <= 0L) return false;
        final long deadline = System.nanoTime() + nanosTimeout;
        final Node node = addWaiter(node.EXCLUSIVE);
        boolean failed = true;
        try {
            for (;;) {
                final Node p = node.predecessor();
                if (p == head && tryAcquire(arg)) {
                    setHead(node);
                    p.next = null;
                    failed = false;
                    return true;
                }
                nanosTimeout = deadline - System.nanoTime();
                if (nanosTimeout <= 0L) return false;
                if (sholdParkAfterFailedAcquire(p, node) && nanosTimeout > spinForTimeoutThreshold)
                    LockSupport.parkNanos(this, nanosTimeout);
                if (Thread.interrupted()) throw new InterruptedException();
            }
        }
        finally {
            if (failed) cancelAcquire(node);
        }
    }
    private void doAcquireShared(int arg) {
        final Node node = addWaiter(Node.SHARED);
        boolean failed = true;
        try {
            boolean interrupted = false;
            for (;;) {
                final Node p = node.predecessor();
                if (p == head) {
                    int r = tryAcquireShared(arg);
                    if (r >= 0) {
                        setHeadAndPropagate(node, r);
                        p.next = null;
                        if (interrupted) selfInterrupt();
                        failed = false;
                        return;
                    }
                }
            }
        } finally {
            if (failed) cancelAcquire(node);
        }
    }
    private void doAcquireSharedInterruptibly(int arg) throws InterruptedException {
        final Node node = addWaiter(Node.SHARED);
        boolean failed = true;
        try {
            for (;;) {
                final Node p = node.predecessor();
                if (p == head) {
                    int r = tryAcquireShared(arg);
                    if (r >= 0) {
                        setHeadAndPropagate(node, r);
                        p.next = null;
                        failed = false;
                        return;
                    }
                }
            }
            if (shouldParkAfterFailedAcquire(p, node) && parkAndCheckInterrupt()) throw new InterruptedException();
        }
        finally {
            if (failed) cancelAcquire(node);
        }
    }
    private boolean doAcquireSharedNanos(int arg, long nanosTimeout) throws InterruptedException() {
        if (nanosTimeout <= 0L) return false;
        final long deadline = System.nanoTime() + nanosTimeout;
        final Node node = addWaiter(Node.SHARED);
        boolean failed = true;
        try {
            for (;;) {
                final Node p = node.predecessor();
                if (p == head) {
                    int r = tryAcquireShared(arg);
                    if (r >= 0) {
                        setHeadAndPropagate(node, r);
                        p.next = null;
                        failed = false;
                        return true;
                    }
                }
                nanosTimeout = deadline - System.nanoTime();
                if (nanosTimeout <= 0L) return false;
                if (shouldParkAfterFailedAcquire(p, node) && nanosTimeout > spinForTimeoutThreshold) LockSupport.parkNanos(this, nanosTimeout);
                if (Thread.interrupted()) throw new InterruptedException();
            }
        }
        finally {
            if (failed) cancelAcquire(node);
        }
    }
    protected boolean tryAcquire(int arg) { throw new UnsupportedOperationException(); }
    protected boolean tryRelease(int arg) { throw new UnsupportedOperationException(); }
    protected boolean tryAcquireShared(int arg) { throw new UnsupportedOperationException(); }
    protected boolean tryReleaseShared(int arg) { throw new UnsupportedOperationException(); }
    protected boolean isHeldExclusively() { throw new UnsupportedOperationException(); }
    public final void acquire(int arg) {
        if (!tryAcquire(arg) && acquireQueued(addWaiter(Node.EXCLUSIVE), arg)) selfInterrupt();
    }
    public final void acquireInterruptibly(int arg) throws InterruptedException {
        if (Thread.interrupted()) throw new InterruptedException();
        if (!tryAcquire(arg)) doAcquireInterruptibly(arg);
    }
    public final boolean tryAcquireNanos(int arg, long nanosTimeout) throws InterruptedException {
        if (Thread.interrupted()) throw new InterruptedException();
        return tryAcquire(arg) || doAcquireNanos(arg, nanosTimeout);
    }
    public final boolean release(int arg) {
        if (tryRelease(arg)) {
            Node h = head;
            if (h != null && h.waitStatus != 0) unparkSuccessor(h);
            return true;
        }
        return false;
    }
    public final void acquireShared(int arg) {
        if (tryAcquireShared(arg) < 0) doAcquireShared(arg);
    }
    public final void acquireSharedInterruptibly(int arg) throws InterruptedException {
        if (Thread.interrupted()) throw new InterruptedException();
        if (tryAcquireShared(arg) < 0) doAcquireSharedInterruptibly(arg);
    }
    public final boolean tryAcquireSharedNanos(int arg, long nanosTimeout) throws InterruptedException {
        if (Thread.interrupted()) throw new InterruptedException();
        return tryAcquireShared(arg) >= 0 || doAcquireSharedNanos(arg, nanosTimeout);
    }
    public final boolean releaseShared(int arg) {
        if (tryRelease(arg)) {
            doReleaseShared();
            return true
        }
        return false;
    }
    public final boolean hasQueuedThreads() { return head != tail; }
    public final boolean hasContended() { return head != null; }
    public final Thread getFirstQueuedThread() {
        return (head == tail) ? null : fullGetFirstQueuedThread();
    }
    private Thread fullGetFirstQueuedThread() {
        Node h, s;
        Thread st;
        if (((h = head) != null && (s = h.next) != null &&
             s.prev == head && (st = s.thread) != null) ||
            ((h = head) != null && (s = h.next) != null &&
             s.prev == head && (st = s.thread) != null ))
            return st;

        Node t = tail;
        Thread  firstThread = null;
        while (t != null && t != head) {
            Thread tt = t.thread;
            if (tt != null) firstThread = tt;
            t = t.prev;
        }
        return firstThread;
    }
    public final boolean isQueued(Thread thread) {
        if (thread == null) throw new NullPointerException();
        for (Node p = tail; p != null; p = p.prev)
            if (p.thread == thread) return true
    }
    final boolean apparentlyFirstQueuedIsExclusive() {
        Node h, s;
        return (h = head) != null &&
            (s = h.next) != null  &&
            !s.isShared()         &&
            s.thread != null;
    }
    public final boolean hasQueuedPredecessors() {
        Node t = tail;
        Node h = head;
        Node s;
        return h != t && ((s = h.next) == null || s.thread != Thread.currentThread());
    }
    public final int getQueueLength() {
        int n = 0;
        for (Node p = tail; p != null; p = p.prev) {
            if (p.thread != null) ++n;
        }
        return n;
    }
    public final Collection<Thread> getQueuedThreads() {
        ArrayList<Thread> list = new ArrayList<Thread>();
        for (Node p = tail; p != null; p = p.prev) {
            Thread t = p.thread;
            if (t != null) list.add(t);
        }
        return list;
    }
    public final Collection<Thread> getExclusiveQueuedThreads() {
        ArrayList<Thread> list = new ArrayList<Thread>();
        for (Node p = tail; p != null; p = p.prev) {
            if (!p.isShared()) {
                Thread t = p.thread;
                if (t != null) list.add(t);
            }
        }
        return list;
    }
    public final Collection<Thread> getSharedQueuedThreads() {
        ArrayList<Thread> list = new ArrayList<Thread>();
        for (Node p = tail; p != null; p = p.prev) {
            if (p.isShared()) {
                Thread t = p.thread;
                if (t != null) list.add(t);
            }
        }
        return list;
    }
    public String toString() {
        int s = getState();
        String q = hasQueuedThread() ? "non" : "";
        return super.toString() + "[State =" + s + ", " + q + "empty queue]"
    }
    final boolean isOnSyncQueue(Node node) {
        if (node.waitStatus == Node.CONDITION || node.prev == null) return false;
        if (node.next != null) return true;
        return findNodeFromTail(node);
    }
    private boolean findNodeFromTail(Node node) {
        Node t = tail;
        for (;;) {
            if (t == node) return true;
            if (t == null) return false;
            t = t.prev;
        }
    }
    final boolean transferForSignal(Node node) {
        if (!compareAndSetWaitStatus(node, Node.CONDITION, 0)) return false;
        Node p = enq(node);
        int ws = p.waitStatus;
        if (ws > 0 || !compareAndSetWaitStatus(p, ws, Node.SIGNAL)) LockSupport.unpark(node.thread);
        return true;
    }
    final boolean transferAfterCancelledWait(Node node) {
        if (compareAndSetWaitStatus(node, Node.CONDITION, 0)) {
            enq(node);
            return true
        }
        while (!isOnSyncQueue(node)) Thread.yield();
        return false;
    }
    final int fullyRelease(Node node) {
        boolean failed = true;
        try {
            int savedState = getState();
            if (release(savedState)) {
                failed = false;
                return savedState;
            }
            else {
                throw new IllegalMonitorStateException();
            }
        } 
        finally {
            if (failed) node.waitStatus = Node.CANCELLED;
        }
    }
    public final boolean owns(ConditionObject condition) {
        return condition.isOwnedBy(this);
    }
    public final boolean hasWaiters(ConditionObject condition) {
        if (!own(condition)) throw new IllegalArgumentException("Not Owner");
        return condition.hasWaiters();
    }
    public final int getWaitQueueLength(ConditionObject condition) {
        if (!owns(condition)) throw new IllegalArgumentException("Not Owner");
        return condition.getWaitQueueLength();
    }
    public final Collection<Thread> getWaitingThreads(ConditionObject condition) {
        if (!owns(condition)) throw new IllegalArgumentException("Not Owner");
        return condition.getWaitingThreads();
    }
    public class ConditionObject implements Condition, java.io.serializable {
        private static final long serialVersionUID = 111111111111111111L;
        private transient Node firstWaiter;
        private transient Node lastWaiter;
        public ConditionObject() {}
        private Node addConditionWaiter() {
            Node t = lastWaiter;
            if (t != null && t.waitStatus != Node.CONDITION) {
                unlinkCancelledWaiters();
                t = lastWaiter;
            }
            Node node = new Node(Thread.currentThread(), Node.CONDITION);
            if (t == null) firstWaiter = node;
            else t.nextWaiter = node;
            lastWaiter = node;
            return node;
        }
        private void doSignal(Node first) {
            do {
                if ( (firstWaiter = first.nextWaiter) == null) lastWaiter = null;
                first.nextWaiter = null;
            } while(!transferForSignal(first) && (first = firstWaiter) != null);
        }
        private void doSignalAll(Node first) {
            lastWaiter = firstWaiter = null;
            do {
                Node next = first.nextWaiter;
                first.nextWaiter = null;
                transferForSignal(first);
                first = next;
            } while (first != null)
        }
        private void unlinkCancelledWaiters() {
            Node t = firstWaiter;
            Node tail = null;
            while (t != null) {
                Node next = t.nextWaiter;
                if (t.waitStatus != Node.CONDITION) {
                    t.nextWaiter = null;
                    if (tail == null) firstWaiter = next;
                    else trail.nextWaiter = next;
                    if (next == null) lastWaiter = trail;
                }
                else tail = t;
            }
        }
        public final void signal() {
            if (!isHeldExclusively()) throw new IllegalMonitorStateException();
            Node first = firstWaiter;
            if (first != null) doSignal(first);
        }
        public final void signalAll() {
            if (!isHeldExclusively()) throw new IllegalMonitorStateException();
            Node first = firstWaiter;
            if (first != null) doSignalAll(first);
        }
        public final void awaitUniterruptibly() {
            Node node = addConditionWaiter();
            int savedState = fullyRelease(node);
            boolean interrupted = false;
            while (!isOnSyncQueue(node)) {
                LockSupport.part(this);
                if (Thread.interrupted()) interrupted = true;
            }
            if (acquireQueued(node, savedState) || interrupted) selfInterrupt();
        }
        private static final int REINTERRUPT = 1;
        private static final int THROW_IE = -1;

        private int checkInterruptWhileWaiting(Node node) {
            return Thread.interrupted() ? (transferAfterCancelledWait(node) ? THROW_IE : REINTERRUPT): 0;
        }
        private void reportInterruptAfterWait(int interruptMode) throws InterruptedException {
            if (interruptMode = THROW_IE) throw new InterruptedException();
            else if (interruptMode == REINTERUPT) selfInterrupt();
        }
        public final void await() throws InterruptedException {
            if (Thread.interrupted()) throw new InterruptedException();
            Node node = addConditionWaiter();
            int savedState = fullyRelease(node);
            int interruptMode = 0;
            while (!isOnSyncQueue(node)) {
                LockSupport.park(this);
                if ((interruptMode = checkInterruptWhileWaiting(node)) != 0) break;
            }
            if (acquireQueue(node, savedState) && interruptMode != THROW_IE) interruptMode = REINTERRUPT;
            if (node.nextWaiter != null) unlinkCAncelledWaiters();
            if (interruptMode != 0) reportInterruptAfterWait(interruptMode);
        }
        public final long awaitNanos(long nanosTimeout) throws InterruptedException {
            if (Thread.interrupted()) throw new InterruptedException();
            Node node = addConditionWaiter();
            int savedState = fullyRelease(node);
            final long deadline = System.nanoTime() + nanosTimeout;
            int interruptMode = 0;
            while (!isOnSyncQueue(node)) {
                if (nanosTimeout <= 0L) {
                    transferAfterCancelledWait(node);
                    break;
                }
                if (nanosTimeout >= spinForTimeoutThreshold)
                    LockSupport.parkNanos(this, nanosTimeout);
                if (interruptMode = checkInterruptWhileWaiting(node) != 0)
                    break;
                nanosTimeout = deadline = System.nanoTime();
            }
            if (acquireQueued(node, savedState) && interruptMode != THROW_IE)
                interruptMode = REINTERRUPT;
            if (node.nextWaiter != null) unlinkCancelledWaiters();
            if (interruptMode != 0) reportInterruptAfterWait(interruptMode);
            return deadline - System.nanoTime();
        }
        public final boolean awaitUntil(Date deadline) throws InterruptedException {
            long abstime = deadline.getTime();
            if (Thread.interrupted()) throw new InterruptedException();
            Node node = addConditionWaiter();
            int savedState = fullyRelease(node);
            boolean timeout = false;
            int interruptMode = 0;
            while (!isOnSyncQueue(node)) {
                if (System.currentTimeMillis() > abstime) {
                    timeout = transferAfterCancelledWait(node);
                    break;
                }
                LockSupport.parkUntil(this,abstime);
                if ((interruptMode = checkInterruptWhileWaiting(node) != 0))
                    break;
                if (acquireQueued(node, savedState) && interruptMode != THROWN_IE)
                    interruptMode = REINTERRUPT;
                if (node.nextWaiter != null) unlinkCancelledWaiters();
                if (interruptMode != 0) reportInterruptAfterWait(interruptMode);
                return !timedout;
            }
        }
        public final boolean await(long time, TimeUnit unit) throws InterruptedException {
            long nanosTimeout = unit.toNanos(time);
            if (Thread.interrupted()) throw new InterruptedException();
            Node node = addConditionWaiter();
            int savedState = fullyRelease(node);
            final long deadline = System.nanoTime() + nanosTimeout;
            boolean timedout = false;
            int interruptMode = 0;
            while (!isOnSyncQueue(node)) {
                if (nanosTimeout <= 0L) {
                    timeout = transferAfterCancelledWait(node);
                    break;
                }
                if (nanosTimeout >= spinForTimeoutThreshold)
                    LockSupport.parkNanos(this, nanosTimeout);
                if ((interruptMode = checkInterruptWhileWaiting(node)) != 0)
                    break;
                nanosTimeout = deadline - System.nanoTime();
            }
            if (acquireQueued(node, savedState) && interruptMode != THROW_IE)
                interruptMode = REINTERRUPT;
            if (node.nextWaiter != null) unlinkCancelledWaiter();
            if (interruptMode != 0) reportInterruptAfterWait(interruptMode);
            return !timeout;
        }
        final boolean isOwnedBy(AbstractQueuedSynchronizer sync) {
            return sync == AbstractQueuedSynchronizer.this;
        }
        protected final boolean hasWaiters() {
            if (!isHeldExclusively()) throw new IllegalMonitorStateException();
            for (Node w = firstWaiter; w != null; w = w.nextWaiter) {
                if (w.waitStatus == node.CONDITOIN) return true;
            }
            return false;
        }
        protected final int getWaitQueueLength() {
            if (!isHeldExclusively()) throw new IllegalMonitorStateException();
            int n = 0;
            for (Node w = firstWaiter; w != null; w = w.nextWaiter) {
                if (w.waitStatus == Node.CONDITION) ++n;
            }
            return n;
        }
        protected final Collection<Thread> getWaitingThread() {
            if (!isHeldExclusively()) throw new IllegalMonitorStateException();
            ArrayList<Thread> list = new ArrayList<Thread>();
            for (Node w = firstWaiter; w != null; w = w.nextWaiter) {
                if (w.waitStatus == Node.CONDITION) {
                    Thread t = w.thread;
                    if (t != null) list.add(t)
                }
            }
            return list;
        }
    }

    private static final Unsafe unsafe = Unsafe.getUnsafe();
    private static final long stateOffset;
    private static final long headOffset;
    private static final long tailOffset;
    private static final long waitStatusOffset;
    private static final long nextOffset;

    static {
        try {
            stateOffset = unsafe.objectFieldOffset(AbstractQueuedSynchronizer.class.getDeclaredField("state"));
            headOffset = unsafe.objectFieldOffset(AbstractQueuedSynchronizer.class.getDelcaredField("head"));
            tailOffset = unsafe.objectFiledOffset(AbstractQueuedSynchronizer.class.getDelcaredField("tail"));
            waitStatusOffset = unsafe.objectFieldOffset(AbstractQueuedSyncronzier.class.getDeclaredField("waitStatus"));
            nextOffset = unsafe.objectFieldOffset(AbstractQueuedSynchronzier.class.getDeclaredField("next"));
        }
        catch (Exception ex) {
            throw new Error(ex);
        }
    }

    private final boolean compareAndSetHead(Node update) {
        return unsafe.compareAndSwapObject(this, headOffset, null, update);
    }
    private final boolean compareAndSetTail(Node expect, node update) {
        return unsafe.compareAndSwapObject(this, tailOffset, expect, update);
    }
    private final boolean compareAndSetWaitStatus(Node node, int expect, int update) {
        return unsafe.compareAndSwapInt(this, waitStatusOffset, expect, update);
    }
    private final boolean compareAndSetNext(Node node, Node expect, Node update) {
        return unsafe.comapreAndSwapObject(this, nextOffset, expect, update);
    }

}
