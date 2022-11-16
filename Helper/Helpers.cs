using System.Text;

namespace MBC_Lux.Helpers
{
   class StringHelpers
   {
      public static string ConvertArrayToString<T>(T[] arr)
      {
         var sb = new StringBuilder();
         sb.Append("[");
         foreach (T e in arr)
         {
            if (e is null)
               continue;
            sb.Append(e.ToString());
            sb.Append(", ");
         }
         sb.Remove(sb.Length - 2, 2);
         sb.Append("]");
         return sb.ToString();
      }
      StringHelpers() { }
   }
}