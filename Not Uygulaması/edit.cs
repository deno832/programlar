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
    public partial class edit_ucontrol : UserControl
    {
        public static int rows_id;
        public edit_ucontrol(string row_id)
        {
            rows_id = Convert.ToInt32(row_id);
            InitializeComponent();
            string connectionString = @"Data Source=C:\Users\Deniz Eren YILDIRIM\Documents\veri_tabanları\notes.db;Version=3;";

            using (SQLiteConnection connection = new SQLiteConnection(connectionString))
            {
                connection.Open();

                // Tablodaki tüm verileri seçen sorgu
                string selectQuery = $"SELECT * FROM Notlar WHERE rowid = {row_id}";

                // SQLiteCommand nesnesi oluşturun ve sorguyu çalıştırın
                using (SQLiteCommand command = new SQLiteCommand(selectQuery, connection))
                {
                    // SQLiteDataReader nesnesini kullanarak sorgu sonuçlarını okuyun
                    using (SQLiteDataReader reader = command.ExecuteReader())
                    {
                        // Satırları okuyarak verileri yazdır
                        while (reader.Read())
                        {
                            baslik_entry.Text = reader[0].ToString();
                            not_entry.Text = reader[1].ToString();
                        }
                    }
                }

                connection.Close();
            }

        }

        private void edit_Load(object sender, EventArgs e)
        {

        }

        private void label1_Click(object sender, EventArgs e)
        {
            
        }

        private void label2_Click(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {
            Application.Restart();
        }

        private void del_btn_Click(object sender, EventArgs e)
        {
            string connectionString = @"Data Source=C:\Users\Deniz Eren YILDIRIM\Documents\veri_tabanları\notes.db;Version=3;";

            using (SQLiteConnection connection = new SQLiteConnection(connectionString))
            {
                connection.Open();

                string selectQuery = $"DELETE FROM Notlar WHERE rowid = {rows_id}";

                using (SQLiteCommand command = new SQLiteCommand(selectQuery, connection))
                {

                    command.ExecuteNonQuery();
                }

                connection.Close();
            }
            MessageBox.Show("Not Başarıyla Silindi!", "İşlem Başarılı!", MessageBoxButtons.OK, MessageBoxIcon.Information);
        }

        private void save_btn_Click(object sender, EventArgs e)
        {
            string connectionString = @"Data Source=C:\Users\Deniz Eren YILDIRIM\Documents\veri_tabanları\notes.db;Version=3;";

            using (SQLiteConnection connection = new SQLiteConnection(connectionString))
            {
                connection.Open();

                string selectQuery = $"UPDATE Notlar SET Baslik = '{baslik_entry.Text}', \"Not\" = '{not_entry.Text}' WHERE rowid = {rows_id}";

                using (SQLiteCommand command = new SQLiteCommand(selectQuery, connection))
                {

                    command.ExecuteNonQuery();
                }

                connection.Close();
            }
            MessageBox.Show("Not Başarıyla Düzenlendi!", "İşlem Başarılı!", MessageBoxButtons.OK, MessageBoxIcon.Information);
        }
    }
}
