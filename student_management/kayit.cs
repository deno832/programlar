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
using static System.Net.Mime.MediaTypeNames;
using static System.Windows.Forms.VisualStyles.VisualStyleElement;

namespace student_managment
{
    public partial class kayit : UserControl
    {
        public kayit()
        {
            InitializeComponent();
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
        }

        private void kayit_Load(object sender, EventArgs e)
        {

        }

        private void save_btn_Click(object sender, EventArgs e)
        {
            string sınıf_düzeyi = "";
            char[] charArray;
            string şube = "";

            string connectionString = "Host=localhost;Port=54321;Database=okul_yönetimi;Username=postgres;Password=2008deno";

            string ad = ad_entry.Text;
            string soyad = soyad_entry.Text;
            string bolum = bolum_box.SelectedItem?.ToString();
            string sınıf = sinif_box.SelectedItem?.ToString();

            
            if (sınıf != null)
            {
                sınıf_düzeyi = sınıf.Remove(sınıf.Length - 1);
                charArray = sınıf.ToCharArray();
                şube = charArray[charArray.Length - 1].ToString();
            }
            else
            {
                MessageBox.Show("Öğrenci Bilgileri Eksik!", "Eksik Bilgi!", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            
            


            if (bolum == "" || sınıf_düzeyi == "" || şube == "" || ad == "" || soyad=="")
            {
                MessageBox.Show("Öğrenci Bilgileri Eksik!", "Eksik Bilgi!", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }



            using (var conn = new NpgsqlConnection(connectionString))
            {
                conn.Open();

                using (var cmd = new NpgsqlCommand())
                {
                    cmd.Connection = conn;
                    cmd.CommandText = $"INSERT INTO öğrenciler (adı,soyadı,sınıf_düzeyi,şube,bölüm) VALUES ('{ad}', '{soyad}', '{sınıf_düzeyi}', '{şube}', '{bolum}')";

                    cmd.ExecuteNonQuery();
                }
            }

            MessageBox.Show("Öğrenci Başarıyla Eklendi!", "İşlem Başarılı!", MessageBoxButtons.OK, MessageBoxIcon.Information);

        }

        private void ad_entry_TextChanged(object sender, EventArgs e)
        {

        }

        private void sinif_box_SelectedIndexChanged(object sender, EventArgs e)
        {

        }
    }
}
