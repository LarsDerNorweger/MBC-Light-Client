namespace MBC_Lux.Helpers
{
   public class QueueElement<T>
   {
      public TaskCompletionSource<T> Task;
      public T Payload;
      public QueueElement(TaskCompletionSource<T> task, T payload)
      {
         Task = task;
         Payload = payload;
      }
   }
}