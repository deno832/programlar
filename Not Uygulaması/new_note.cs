using System;
using System.Data.SQLite;
using System.Windows.Forms;

namespace ilk_sqlite_console
{
    public partial class @new : UserControl
    {
        public @new()
        {
            InitializeComponent();
        }

        private void save_btn_Click(object sender, EventArgs e)
        {
            string connectionString = @"Data Source=C:\Users\Deniz Eren YILDIRIM\Documents\veri_tabanları\notes.db;Version=3;";

            using (SQLiteConnection connection = new SQLiteConnection(connectionString))
            {
                connection.Open();

                string selectQuery = $"INSERT INTO Notlar VALUES ('{baslik_entry.Text}','{not_entry.Text}')";

                using (SQLiteCommand command = new SQLiteCommand(selectQuery, connection))
                {

                    command.ExecuteNonQuery();
                }

                connection.Close();
            }
            MessageBox.Show("Not Başarıyla Oluşturuldu", "İşlem Başarılı!", MessageBoxButtons.OK, MessageBoxIcon.Information);
        }

        private void not_entry_TextChanged(object sender, EventArgs e)
        {

        }

        private void exit_btn_Click(object sender, EventArgs e)
        {
            Application.Restart();
        }
    }
}
