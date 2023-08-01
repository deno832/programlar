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
    public partial class görüntüle : UserControl
    {
        public görüntüle()
        {
            InitializeComponent();
        }

        private void görüntüle_Load(object sender, EventArgs e)
        {
            string connectionString = "Host=localhost;Username=postgres;Password=2008deno;Port=54321;Database=okul_yönetimi";
            datatable.AutoSizeRowsMode = DataGridViewAutoSizeRowsMode.AllCells;
            datatable.AutoSizeColumnsMode = DataGridViewAutoSizeColumnsMode.AllCells;
            using (NpgsqlConnection connection = new NpgsqlConnection(connectionString))
            {
                try
                {
                    connection.Open();
                    
                    // Veritabanından verileri çekmek için bir sorgu oluşturun
                    string query = "SELECT * FROM öğrenciler";

                    using (NpgsqlDataAdapter adapter = new NpgsqlDataAdapter(query, connection))
                    {
                        DataSet dataSet = new DataSet();

                        // Verileri DataSet'e yükleyin
                        adapter.Fill(dataSet);

                        // DataGridView'e DataSet'teki verileri bağlayın
                        datatable.DataSource = dataSet.Tables[0];
                    }
                }
                catch (Exception ex)
                {
                    MessageBox.Show("Veriler yüklenirken bir hata oluştu: " + ex.Message);
                }
                finally
                {
                    connection.Close();
                }
            }
        }

        private void datatable_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }
    }
}
