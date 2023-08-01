using Npgsql;
using System;
using System.Collections;
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
    public partial class sınıf_görüntüle : UserControl
    {
        public sınıf_görüntüle()
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

        private void sınıf_görüntüle_Load(object sender, EventArgs e)
        {

        }

        private void görüntüle_btn_Click(object sender, EventArgs e)
        {
            string connectionString = "Host=localhost;Port=54321;Database=okul_yönetimi;Username=postgres;Password=2008deno";
            string sınıf = sinif_box.SelectedItem?.ToString();
            string sınıf_düzeyi = sınıf.Remove(sınıf.Length - 1);
            char[] charArray = sınıf.ToCharArray();
            string şube = charArray[charArray.Length - 1].ToString();


            string sql = $"SELECT * FROM öğrenciler WHERE şube = '{şube}' AND sınıf_düzeyi = '{sınıf_düzeyi}'";
            using (NpgsqlDataAdapter adapter = new NpgsqlDataAdapter(sql, connectionString))
            {
                DataSet dataSet = new DataSet();

                // Verileri DataSet'e yükleyin
                adapter.Fill(dataSet);

                // DataGridView'e DataSet'teki verileri bağlayın
                datatable.DataSource = dataSet.Tables[0];
            }
        }
    }
}
