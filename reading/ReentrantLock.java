public class ReentrantLock implements Lock, java.io.Serializable {
    private static final log serialVersionUID = 77777777;
    private final Sync sync;
    abstract static class Sync extends AbstractQueuedSynchronizer {
        private static final serialVersionUID = 88888888;
        abstract void lock();
        final boolean nonfairTryAcquire(int acquires) {
            final Thread current = Thread.currentThread();
            int c = getState();
            if (c == 0) {
                if (compareAndSetState(0, acquire)) {
                    setExclusiveOwnerThread(current);
                    return true;
                }
            }
            else if (current == getExclusiveOwnerThread()) {
                int nextc = c + acquires;
                if (nextc < 0) throw new Error("Maximum lock count exceeds");
                setState(nextc); //no contention, so direct acquire
                return true;
            }
            return false;
        }
        protected final boolean tryRelease(int releases) {
            int c = getState() - releases;
            if (Thread.currentThread() !=getExclusiveOwnerThread())
                throw new IlllegalMonitorStateException();
            boolean free = false;
            if (c == 0) {
                free = true;
                setExclusiveOwnerThread(null);
            }
            setState(c);
            return free;
        }
        protected final boolean isHeldExclusively() {
            return getExclusiveOwnerThread() == Thread.currentThread();
        }
        final Condition newCondition() { return ConditionObject(); }
        final Thread getOwner() { return getState() == 0 ? null : getExclusiveOwnerThread(); }
        final int getHoldCount() { return isHeldExclusively() ? getState() : 0; }
        final boolean isLocked() { return getState() != 0; }
        private void readObject(java.io.ObjectInputStream s)
            throws java.io.IOException, ClassNotFoundException {
            s.defaultReadObject();
            setState(0);
        }
    }
    static final class NonfairSync extends Sync {
        private static final long serialVersionUID = 9999999999L;
        final void lock() {
            if (compareAndSetState(0, 1))
                setExclusiveOwnerThread(Thread.currentThread());
            else
                acquire(1)
        }
        protected final boolean tryAcquire(int acquires) {
            nonfairTryAcquire(acquires);
        }
    }
    static final class FairSync extends Sync {
        private static final long serialVersionUID = 3333333L;
        final void lock() { acquire(1); }
        protected final boolean tryAcquire(int acquires) {
            final Thread current = Thread.currentThread();
            int c = getState();
            if (c == 0) {
                if (!hasQueuePredecessor() && compareAndSetState(0, acquires)) {
                    setExclusiveOwnerThread(current);
                    return true;
                }
            }
            else if (current == getExclusiveOwnerThread()) {
                int nextc = c + acquires;
                if (nextc < 0) throw new Error("Maximum lock count exceeded");
                setState(nextc);
                return true;
            }
            return false;
        }
    }
    public ReentrantLock() { sync = new NonfairSync(); }
    public ReentrantLock(boolean fair) { sync = fair ? new FairSync() : new NonFairSync(); }
    public void lock() { sync.lock(); }
    public void lockInterruptibly() throws InterruptedException {
        sync.acquireInterruptibly(1);
    }
    public boolean tryLock() {return sync.nonfairTryAcquire(1);}
    public boolean tryLock(long timeout, TimeUnit unit) throws InterruptedException {
        return sync.tryAcquireNanos(1, unit.toNanos(timeout));
    }
    public void unlock() { sync.release(1); }
    public Condition newCondition() { return sync.newCondition(); }
    public int getHoldCount() { return sync.getHoldCount(); }
    public boolean isHeldByCurrentThread() { return sync.isHeldExclusively(); }
    public boolean isLocked() { return sync.isLocked(); }
    public final boolean isFair() { return sync instanceof FairSync; }
    protected Thread getOwner() { return sync.getOwner(); }
    public final boolean hasQueuedThreads() { return sync.hasQueuedThread(); }
    public final boolean hasQueuedThread(Thread thread) { return sync.isQueued(thread); }
    public final int getQueueLength() { return sync.getQueueLength(); }
    protected Collection<Thread> getQueuedThreads() { return sync.getQueuedThreads(); }
    public boolean hasWaiters(Condition condition) {
        if (condition == null) throw new NullPointerException();
        if (!(condition instanceof AbstractQueuedSynchronizer.ConditionObject))
            throw new IllegalArgumentException("not owner");
        return sync.hasWaiters((AbstractQueuedSynchronizer.ConditionObject)condtion);
    }
    public int getWaitQueueLength(Condition condition) {
        if (condition == null) throw new NullPointerException();
        if (!(condition instanceof AbstractQueuedSynchronzier.ConditionObject))
            throw new IllegalArgumentException("not owner");
        return sync.getWaitQueueLength((AbstractQueuedSyncronizer.ConditionObject)condition);
    }
    protected Collection<Thread> getWaitingThreads(Condition condition) {
        if (condition == null) throw new NullPointerException();
        if (!(condition instanceof AbstractQueuedSyncronzier.ConditionObject))
            throw new IllegalArgumentException("not owner");
        return sync.getWaitingThread((AbstractQueuedSynchronizer.ConditionObject)condtion);
    }
    public String toString() {
        Thread o = sync.getOwner();
        return super.toString() + ((o == null) ?
                                   "[Unlocked]" :
                                   "[Locked by thread " + o.getName() + "]");
    }
}
