namespace MBC_Lux.Helpers
{
   public class CustomQueue<T>
   {
      public bool isEmpty { get => m_Queue.Count() <= 0; }
      public CustomQueue()
      {
         m_Queue = new();
      }

      public TaskCompletionSource<T>? DeQueue()
      {
         if (isEmpty)
            return null;
         return m_Queue.Dequeue().Task;
      }
      public T? peek(T? def)
      {
         if (isEmpty)
            return def;
         var res = m_Queue.Peek();
         return res.Payload;
      }
      public Task<T> EnQueue(T element)
      {
         var t = new TaskCompletionSource<T>();
         m_Queue.Enqueue(new QueueElement<T>(t, element));
         return t.Task;
      }
      Queue<QueueElement<T>> m_Queue;
   }
}