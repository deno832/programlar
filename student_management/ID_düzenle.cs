using Npgsql;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using static Npgsql.Replication.PgOutput.Messages.RelationMessage;

namespace student_managment
{
    public partial class ID_düzenle : Form
    {
        public static string idmiz;
        public ID_düzenle(string id, string ad, string soy_ad, string düzey,string şube,string bölüm)
        {
            InitializeComponent();
            idmiz = id;
            string connectionString = "Host=localhost;Port=54321;Database=okul_yönetimi;Username=postgres;Password=2008deno";

            using (var conn = new NpgsqlConnection(connectionString))
            {
                conn.Open();

                string sql = "SELECT * FROM sınıflar";

                using (var cmd = new NpgsqlCommand(sql, conn))
                {
                    using (var reader = cmd.ExecuteReader())
                    {
                        while (reader.Read())
                        {
                            for (int i = 1; i < reader.FieldCount; i += 4)
                            {
                                string text = reader.GetString(i) + reader.GetString(i + 1);
                                sinif_box.Items.Add(text);
                            }
                        }
                    }
                }
            }

            ad_entry.Text = ad;
            soyad_entry.Text = soy_ad;
            sinif_box.SelectedItem = düzey+şube;
            bolum_box.SelectedItem = bölüm;
        }

        private void ID_düzenle_Load(object sender, EventArgs e)
        {

        }

        private void save_btn_Click(object sender, EventArgs e)
        {
            string connectionString = "Host=localhost;Port=54321;Database=okul_yönetimi;Username=postgres;Password=2008deno";

            using (var conn = new NpgsqlConnection(connectionString))
            {
                conn.Open();

                using (var cmd = new NpgsqlCommand())
                {
                    cmd.Connection = conn;
                    
                    string sınıf_düzeyi = "";
                    char[] charArray;
                    string şube = "";

                    string sınıf = sinif_box.SelectedItem?.ToString();
                    sınıf_düzeyi = sınıf.Remove(sınıf.Length - 1);
                    charArray = sınıf.ToCharArray();
                    şube = charArray[charArray.Length - 1].ToString();

                    cmd.CommandText = $"UPDATE öğrenciler SET adı = '{ad_entry.Text}', soyadı = '{soyad_entry.Text}',sınıf_düzeyi = '{sınıf_düzeyi}',şube = '{şube}',bölüm = '{bolum_box.SelectedItem?.ToString()}' WHERE id = {idmiz}";

                    cmd.ExecuteNonQuery();
                }
                MessageBox.Show("Veri başarıyla Düzenlendi!", "İşlem Başarılı!", MessageBoxButtons.OK, MessageBoxIcon.Information);

            }
        }

        private void sil_btn_Click(object sender, EventArgs e)
        {
            string connectionString = "Host=localhost;Port=54321;Database=okul_yönetimi;Username=postgres;Password=2008deno";

            using (var conn = new NpgsqlConnection(connectionString))
            {
                conn.Open();

                using (var cmd = new NpgsqlCommand())
                {
                    cmd.Connection = conn;

                    cmd.CommandText = $"DELETE FROM öğrenciler WHERE id = {idmiz}";

                    cmd.ExecuteNonQuery();
                }
                MessageBox.Show("Öğrenci Başarıyla Silindi!!", "İşlem Başarılı!", MessageBoxButtons.OK, MessageBoxIcon.Information);
                this.Close();
            }
        }
    }
}
