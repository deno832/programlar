using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using Npgsql;

namespace student_managment
{
    public partial class sinif_edit : Form
    {
        static public int idsi;
        public sinif_edit(int id)
        {
            InitializeComponent();
            idsi = id;
            string connectionString = "Host=localhost;Port=54321;Database=okul_yönetimi;Username=postgres;Password=2008deno";

            using (var conn = new NpgsqlConnection(connectionString))
            {
                conn.Open();

                string sql = $"SELECT * FROM sınıflar WHERE id = {id}";

                using (var cmd = new NpgsqlCommand(sql, conn))
                {
                    using (var reader = cmd.ExecuteReader())
                    {
                       if (reader.Read())
                       {
                            string bolum = reader.GetString(0);
                            string duzey = reader.GetString(1);
                            string sube = reader.GetString(2);

                            bolum_box.SelectedItem = bolum;
                            duzey_box.SelectedItem = duzey;
                            şube_entry.Text = sube;
                        }
                    }
                }
            }
        }

        private void sinif_edit_Load(object sender, EventArgs e)
        {

        }

        private void delete_btn_Click(object sender, EventArgs e)
        {
            string bolum = bolum_box.SelectedItem?.ToString();
            string duzey = duzey_box.SelectedItem?.ToString();
            string şube = şube_entry.Text;
            
            string connectionString = "Host=localhost;Port=54321;Database=okul_yönetimi;Username=postgres;Password=2008deno";

            string sql = $"SELECT * FROM öğrenciler WHERE sınıf_düzeyi = '{duzey}' AND şube = '{şube}'";

            bool dolu_mu = VeriVarMi(connectionString,sql);
            if (dolu_mu)
            {
                MessageBox.Show("Bu Sınıfa Kayıtlı Bir Öğrenci Var!", "Sınıf Dolu!", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

            using (var conn = new NpgsqlConnection(connectionString))
            {
                conn.Open();

                string sorgu = $"DELETE FROM sınıflar WHERE id = {idsi}";

                using (var cmd = new NpgsqlCommand(sorgu, conn))
                {
                    cmd.ExecuteNonQuery();
                    MessageBox.Show("Sınıf Başarıyla Silindi!", "İşlem Başarılı!", MessageBoxButtons.OK, MessageBoxIcon.Information);
                    this.Close();
                }
            }
        }

        public bool VeriVarMi(string connectionString, string sorgu)
        {
            using (NpgsqlConnection conn = new NpgsqlConnection(connectionString))
            {
                conn.Open();

                using (NpgsqlCommand command = new NpgsqlCommand(sorgu, conn))
                {
                    // Veriyi sorgulayın
                    using (NpgsqlDataReader reader = command.ExecuteReader())
                    {
                        // Eğer veri varsa true döndürün, aksi halde false döndürün
                        return reader.HasRows;
                    }
                }
            }
        }

        private void edit_btn_Click(object sender, EventArgs e)
        {
            string connectionString = "Host=localhost;Port=54321;Database=okul_yönetimi;Username=postgres;Password=2008deno";
            using (var conn = new NpgsqlConnection(connectionString))
            {
                conn.Open();

                string bolum = bolum_box.SelectedItem?.ToString();
                string duzey = duzey_box.SelectedItem?.ToString();
                string şube = şube_entry.Text;

                string sql = $"UPDATE sınıflar SET bolum = '{bolum}', sınıf_düzeyi = {duzey}, şube = '{şube}' WHERE id = {idsi}";

                using (var cmd = new NpgsqlCommand(sql, conn))
                {
                    cmd.ExecuteNonQuery();
                    MessageBox.Show("Sınıf Başarıyla Düzenlendi!", "İşlem Başarılı!", MessageBoxButtons.OK, MessageBoxIcon.Information);
                    this.Close();
                }
            }
        }
    }
}
