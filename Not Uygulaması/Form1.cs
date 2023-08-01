using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Data.SQLite;


namespace ilk_sqlite_console
{
    public partial class Form1 : Form
    {
        public static int rowid;
        public Form1()
        {
            InitializeComponent();

            string connectionString = @"Data Source=C:\Users\Deniz Eren YILDIRIM\Documents\veri_tabanları\notes.db;Version=3;";

            using (SQLiteConnection connection = new SQLiteConnection(connectionString))
            {
                connection.Open();

                // Tablodaki tüm verileri seçen sorgu
                string selectQuery = "SELECT rowid,* FROM Notlar";

                // SQLiteCommand nesnesi oluşturun ve sorguyu çalıştırın
                using (SQLiteCommand command = new SQLiteCommand(selectQuery, connection))
                {
                    // SQLiteDataReader nesnesini kullanarak sorgu sonuçlarını okuyun
                    using (SQLiteDataReader reader = command.ExecuteReader())
                    {
                        // Satırları okuyarak verileri yazdır
                        while (reader.Read())
                        {
                            for (int i = 1; i < reader.FieldCount; i+=3)
                            {
                                Button button = new Button();
                                button.Text = reader[i] + "\t";
                                button.Width = 370;
                                button.Height = 30;

                                
                                button.Tag = reader[i-1];
                                
                                button.Click += Button_Click; // Event handler atama,
                                
                                button.Font = new Font("Arial", 12);
                                NotePanel.Controls.Add(button);
                            }
                            Console.WriteLine();
                        }
                    }
                }

                connection.Close();
            }
            int labelCount = 5;

            for (int i = 0; i < labelCount; i++)
            {
            }

        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void flowLayoutPanel1_Paint(object sender, PaintEventArgs e)
        {

        }

        private void Button_Click(object sender, EventArgs e)
        {
            Button clickedButton = (Button)sender;
            string buttonText = clickedButton.Text;
            this.Width = 590;
            this.Height = 710;
            this.Controls.Clear();
            this.Controls.Add(new edit_ucontrol(clickedButton.Tag.ToString()));
            //MessageBox.Show(clickedButton.Tag.ToString());

        }

        private void del_btn_Click(object sender, EventArgs e) //senin ismini sevim
        {
            this.Width = 590;
            this.Height = 710;
            this.Controls.Clear();
            this.Controls.Add(new @new());
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}
