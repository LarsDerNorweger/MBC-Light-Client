namespace MBC_Lux
{
   enum States
   {
      // PROGRAMM
      setGroup = 0x02,

      // OK
      OK = 0xaa,

      // ERROR CODES
      unkown = 0xF1,
      inkonsitentCommand = 0xF2,
      unknownPIN = 0xF2,
      unknownGrp = 0xF2,

   }
}