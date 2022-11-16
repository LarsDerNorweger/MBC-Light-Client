using System.IO.Ports;
using MBC_Lux.Helpers;
namespace MBC_Lux
{

   class Serial
   {
      public delegate void handleMessage(byte[] data);
      public event handleMessage? onMessage;
      public Serial(string port, Baud baud)
      {
         m_SerialPort = new SerialPort(port, (int)baud);
         m_SerialPort.DataReceived += handlebyte;
         m_SerialPort.RtsEnable = true;
         m_Queue = new();
      }

      public Task<byte[]> execute(byte[] data)
      {
         if (m_Queue.isEmpty)
            Send(data);
         return m_Queue.EnQueue(data);
      }

      void handlebyte(object sender, SerialDataReceivedEventArgs e)
      {
         int l = m_SerialPort.BytesToRead;
         byte[] buf = new byte[l];
         m_SerialPort.Read(buf, 0, l);
#if DEBUG
         Console.WriteLine("Serial <= " + StringHelpers.ConvertArrayToString<byte>(buf));
#endif

         if (m_Queue.isEmpty)
         {
            onMessage?.Invoke(buf);
            return;
         }

         var res = m_Queue.DeQueue();
         res?.SetResult(buf);

         if (m_Queue.isEmpty)
            return;

         var next = m_Queue.peek(null);
         if (next is not null)
            Send(next);
      }

      public void Send(byte[] data)
      {
         if (!m_Started)
            throw new InvalidOperationException("SerialPort must be opened");
#if DEBUG
         Console.WriteLine("Serial => " + StringHelpers.ConvertArrayToString<byte>(data));
#endif
         m_SerialPort.Write(data, 0, data.Length);
      }

      public void Start()
      {
         m_Started = true;
         m_SerialPort.Open();
      }
      public void Stop()
      {
         m_Started = false;
         m_SerialPort.Close();
      }


      SerialPort m_SerialPort;
      bool m_Started = false;
      CustomQueue<byte[]> m_Queue;
   }
}