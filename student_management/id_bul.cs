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

namespace student_managment
{
    public partial class id_bul : UserControl
    {
        public static string ad;
        public static string soyad;
        public static string sınıf;
        public static string şubee;
        public static string bölüm;
        public static string id;
        public id_bul()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string connectionString = "Host=localhost;Port=54321;Database=okul_yönetimi;Username=postgres;Password=2008deno";

            string sql = $"SELECT * FROM öğrenciler WHERE id = {ID_entry.Text} ";
            id = ID_entry.Text;
            using (var conn = new NpgsqlConnection(connectionString))
            {
                conn.Open();

                using (var cmd = new NpgsqlCommand(sql, conn))
                {
                    using (var reader = cmd.ExecuteReader())
                    {
                        while (reader.Read())
                        {
                            ad = reader.GetString(1).ToString();
                            soyad = reader.GetString(2).ToString();
                            sınıf = reader.GetString(3).ToString();
                            şubee = reader.GetString(4).ToString();
                            bölüm = reader.GetString(5).ToString();
                            id = ID_entry.Text;

                            ad_lbl.Text = ad;
                            soy_lbl.Text = soyad;
                            string duzey = sınıf;
                            string şube = şubee;
                            sınıf_lbl.Text = duzey+şube;
                            bolum_lbl.Text = bölüm;

                        }
                    }
                }
            }
        }

        private void edit_btn_Click(object sender, EventArgs e)
        {
            ID_düzenle edit_window = new ID_düzenle(id,ad,soyad,sınıf,şubee,bölüm);
            edit_window.FormClosed += EditClosed;
            edit_window.Show();
        }
        private void EditClosed(object sender, EventArgs e)
        {
            this.Controls.Clear();
            id_bul controls = new id_bul();
            this.Controls.Add(controls);
        }
    }
}
