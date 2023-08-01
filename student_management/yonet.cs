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
using static System.Windows.Forms.VisualStyles.VisualStyleElement;
using static System.Windows.Forms.VisualStyles.VisualStyleElement.ToolBar;

namespace student_managment
{
    public partial class yonet : UserControl
    {
        public yonet()
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
                                System.Windows.Forms.Button button = new System.Windows.Forms.Button();

                                string text = reader.GetString(i) + reader.GetString(i + 1);
                                button.Text = reader[i].ToString() + reader[i + 1].ToString() + "\t";
                                button.Width = 235;
                                button.Height = 30;


                                button.Tag = reader.GetInt16(3);

                                button.Click += Sınıf_Button_Click; // Event handler atama,

                                button.Font = new Font("Arial", 12);
                                sınıflar_panel.Controls.Add(button);

                            }



                            //int id = reader.GetInt16(0); // id sütununun indeksi 0'dır
                            //string name = reader.GetString(1); // name sütununun indeksi 1'dir
                            //string password = reader.GetString(2);
                            //Console.WriteLine($"ID: {id},Nickname: {name} ,Passwd: {password}");
                        }
                    }
                }
            }

        }


        private void panel1_Paint(object sender, PaintEventArgs e)
        {

        }
        protected void Sınıf_Button_Click(object sender, EventArgs e)
        {
            System.Windows.Forms.Button clickedButton = (System.Windows.Forms.Button)sender;
            int id = Convert.ToInt32(clickedButton.Tag);
            sinif_edit edit_window = new sinif_edit(id);
            edit_window.Show();
            edit_window.FormClosed += EditClosed;
        }


        private void add_btn_Click(object sender, EventArgs e)
        {
            string connectionString = "Host=localhost;Port=54321;Database=okul_yönetimi;Username=postgres;Password=2008deno";


            string bolum = bolum_box.SelectedItem?.ToString();
            string duzey = duzey_box.SelectedItem?.ToString();
            string şube = şube_entry.Text;

            if (bolum == "" || duzey == "" || şube == "")
            {
                MessageBox.Show("Sınıf Değerleri Eksik!", "Eksik Bilgi!", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }



            using (var conn = new NpgsqlConnection(connectionString))
            {
                conn.Open();

                using (var cmd = new NpgsqlCommand())
                {
                    cmd.Connection = conn;
                    cmd.CommandText = $"INSERT INTO sınıflar (bolum,sınıf_düzeyi,şube) VALUES ('{bolum}', '{duzey}', '{şube}')";

                    cmd.ExecuteNonQuery();
                }
            }

            MessageBox.Show("Sınıf Başarıyla Eklendi!", "İşlem Başarılı!", MessageBoxButtons.OK, MessageBoxIcon.Information);

            this.Controls.Clear();
            this.Controls.Add(new yonet());
        }

        private void EditClosed(object sender, EventArgs e)
        {
            this.Controls.Clear();
            this.Controls.Add(new yonet());
        }

        private void sınıflar_panel_Paint(object sender, PaintEventArgs e)
        {

        }
    }
}
