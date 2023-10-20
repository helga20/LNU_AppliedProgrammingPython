using System;
using System.IO;
using System.Linq;

namespace TestC
{
    class Program
    {
        static void Main(string[] args)
        {
            var path = Path.Combine("Test", "test.txt");
            var text = File.ReadAllLines(path).Last().Split(" ");
            var a = int.Parse(text[1]);
            var b = int.Parse(text[2]);
            var c = a + b;
            File.AppendAllText(path, $"\nSubproces: {b} {c}");

            Console.WriteLine("Press enter to stop subproces");
            Console.ReadKey();
        }
    }
}
