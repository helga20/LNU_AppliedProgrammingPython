using System;
using System.IO;
using System.Linq;
using System.Windows.Forms;
using System.Windows.Forms.DataVisualization.Charting;

namespace script
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            var alphabet = "abcdefghijklmnopqrstuvwxyz0123456789{}:.,()-";
            // Path to file
            var path = @".\result.txt";
            string text;

            // Read file
            using (var file = new StreamReader(path))
            {
                text = file.ReadToEnd();
            }

            // Subprocess count entries of each letter in all file
            using (var file = new StreamWriter(path, true))
            {
                file.WriteLine("\nSubproces result");
                MainChart.Series["Sign"].IsValueShownAsLabel = true;
                
                foreach (var letter in alphabet)
                {
                    var amount = text.ToCharArray().Count(l => l == letter);
                    if (amount > 0)
                    {
                        file.WriteLine($"Letter - {letter}\tamount - {amount}");
                        MainChart.Series["Sign"].Points.AddXY(letter.ToString(), amount);
                    }
                }
                file.WriteLine("");
            }
        }
    }
}
