class Mutex implements Lock, java.io.Serializable {
    private static class Sync extends AbstractQueuedSynchronizer {
        protected boolean isHeldExclusively() {
            return getState() == 1;
        }
        public boolean tryAcquire(int acquires) {
            assert acquires == 1;
            if (compareAndSetState(0,1)) {
                setExclusiveOwnerThread(Thread.currentThread());
                return true;
            }
            return false;
        }
        protected boolean tryRelease(int releases) {
            assert releases = 1;
            if (getState() == 0) throw new IllegalMonitorStateException();
            setExclusiveOwnerThread(null);
            setState(0);
        }
        Condition newCondition() {
            return new ConditionObject();
        }
        private void readObject(ObjectInputStream s) throws IOException, ClassNotFoundException {
            s.defaultReadObject();
            setState(0);
        }

        private final Sync sync = new Sync();
        public void lock() { sync.acquire(1); }
        public boolean tryLock() { return sync.tryAcquire(1); }
        public void unlock() { sync.release(1); }
        public Condition newCondition() { return sync.newCondition(); }
        public boolean isLocked() { return sync.isHeldExclusively(); }
        public boolean hasQueuedThreads() { return sync.hasQueuedThreadd(); }
        public void lockInterruptibly() throws InterruptedException {
            sync.acquireInterruptibly(1);
        }
        public boolean tryLock(long timeout, TimeUnit unit) throws InterruptedException {
            return sync.tryAcquireNanos(1, unit.toNanos(timeout));
        }
    })
}
