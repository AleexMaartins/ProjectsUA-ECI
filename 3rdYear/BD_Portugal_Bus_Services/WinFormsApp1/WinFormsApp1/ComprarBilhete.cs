using Microsoft.Data.SqlClient;
using System;
using System.Data;
using System.Windows.Forms;

namespace WinFormsApp1
{
    public partial class ComprarBilhete : Form
    {
        private menu menu;
        //private string conStr = "Data Source=DESKTOP-RGVE259;Initial Catalog=EAP;Integrated Security=True;TrustServerCertificate=True";
        private string conStr = Globals.strConn;

        public ComprarBilhete(menu menu)
        {
            InitializeComponent();
            this.menu = menu;
        }

        private void ComprarBilhete_Load(object sender, EventArgs e)
        {
            // Initialize components when the form loads.
        }

        private void btnSearch_Click(object sender, EventArgs e)
        {
            string origem = textBox1.Text;
            string destino = textBox2.Text;
            DataTable results = GetViagensPorOrigemDestino(origem, destino);
            dataGridView1.DataSource = results;
        }

        private DataTable GetViagensPorOrigemDestino(string origem, string destino)
        {
            DataTable dt = new DataTable();
            string connectionString = "Data Source=DESKTOP-RGVE259;Initial Catalog=EAP;Integrated Security=True;TrustServerCertificate=True";

            using (SqlConnection conn = new SqlConnection(connectionString))
            {
                using (SqlCommand cmd = new SqlCommand("SELECT DISTINCT * FROM EAP.Horarios(@origem, @destino)", conn))
                {
                    cmd.Parameters.AddWithValue("@origem", origem);
                    cmd.Parameters.AddWithValue("@destino", destino);

                    SqlDataAdapter da = new SqlDataAdapter(cmd);
                    da.Fill(dt);
                }
            }

            return dt;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            string passageiro_id = textBox8.Text;
            string viagem_id = textBox7.Text;
            string origem = textBox6.Text;
            string destino = textBox5.Text;
            //string tipoBagagem = comboBoxTipoBagagem.SelectedItem.ToString();
            //float pesoBagagem = float.Parse(textBoxPesoBagagem.Text);
            //float volumeBagagem = float.Parse(textBoxVolumeBagagem.Text);

            using (SqlConnection con = new SqlConnection(conStr))
            {
                try
                {
                    con.Open();
                    string queryBilhete = "EXEC EAP.ComprarBilhete @passageiro_id, @viagem_id, @origem, @destino";
                    using (SqlCommand cmdBilhete = new SqlCommand(queryBilhete, con))
                    {
                        cmdBilhete.Parameters.AddWithValue("@passageiro_id", passageiro_id);
                        cmdBilhete.Parameters.AddWithValue("@viagem_id", viagem_id);
                        cmdBilhete.Parameters.AddWithValue("@origem", origem);
                        cmdBilhete.Parameters.AddWithValue("@destino", destino);
                        cmdBilhete.ExecuteNonQuery();
                    }

                    DataTable results = Passageiro_Bilhete(passageiro_id);
                    dataGridView2.DataSource = results;
                }
                catch (Exception ex)
                {
                    MessageBox.Show("Error! " + ex.Message);
                }
            }
        }

        private DataTable Passageiro_Bilhete(string passageiro_id)
        {
            DataTable dt = new DataTable();
            string connectionString = "Data Source=DESKTOP-RGVE259;Initial Catalog=EAP;Integrated Security=True;TrustServerCertificate=True";

            using (SqlConnection conn = new SqlConnection(connectionString))
            {
                using (SqlCommand cmd = new SqlCommand("SELECT * FROM EAP.Passageiro_Bilhete(@passageiro_id)", conn))
                {
                    cmd.Parameters.AddWithValue("@passageiro_id", passageiro_id);

                    SqlDataAdapter da = new SqlDataAdapter(cmd);
                    da.Fill(dt);
                }
            }

            return dt;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            menu.Show();
            this.Hide();
        }

        private void dataGridView2_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }
    }
}
