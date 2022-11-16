using System.IO.Ports;

namespace MBC_Lux
{
   class Programm
   {
      async public static Task Main()
      {
         Console.WriteLine("Start");
         var ser = new Serial("/dev/ttyACM0", Baud.slow);
         ser.Start();
         ser.onMessage += handleMessage;

         var res1 = ser.execute(new byte[] { 0x02, 0x01, 0x03 });
         var res2 = ser.execute(new byte[] { 0x02, 0x01, 0x06, 0x05, 0x03 });
         var t1 = await res2;
         var t2 = await res1;
         ser.Stop();
         Console.WriteLine("Close");

      }

      static void handleMessage(byte[] data)
      {
         Console.WriteLine(data);
      }
   }
}