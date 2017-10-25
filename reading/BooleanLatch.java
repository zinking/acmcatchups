class BooleanLatch {
    private static class Sync extends AbstractQueuedSynchronizer {
        boolean isSignaled() { return getState() != 0; }
        protected int tryAcquireShared(int ignore) {
            return isSignalled() ? 1 : -1;
        }
        protected boolean tryReleaseShared(int ignore) {
            setState(1);
            return true;
        }
    }

    private final Sync sync = new Sync();
    public boolean isSignalled() { return sync.isSignalled(); }
    public void signal() { sync.releaseShared(1); }
    public void await() throws InterruptedException {
        sync.acquireSharedInterruptibly(1);
    }
}