using Microsoft.Data.SqlClient;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using static System.Windows.Forms.VisualStyles.VisualStyleElement;


namespace WinFormsApp1
{

    public partial class AddAutocarros : Form
    {
        private ShowAutocarro showAutocarro;
        private string conStr = Globals.strConn;

        //private string conStr = "Data Source=DESKTOP-RGVE259;Initial Catalog=EAP;Integrated Security=True;TrustServerCertificate=True";

        public AddAutocarros(ShowAutocarro showAutocarro)
        {
            InitializeComponent();
            this.showAutocarro = showAutocarro;
            displayModelos();
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox2_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox3_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox4_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox5_TextChanged(object sender, EventArgs e)
        {

        }
        private void button1_Click(object sender, EventArgs e)
        {
            if (int.TryParse(textBox1.Text, out int kms) &&
                int.TryParse(textBox4.Text, out int capacidade) &&
                int.TryParse(textBox2.Text, out int num_lugares) &&
                int.TryParse(textBox5.Text, out int modelo_id))
            {
                string matricula = textBox3.Text;

                using (SqlConnection con = new SqlConnection(conStr))
                {
                    try
                    {
                        con.Open();
                        string query = "EXEC EAP.addAutocarro @kms, @num_lugares, @matricula, @capacidade, @modelo_id";

                        using (SqlCommand cmd = new SqlCommand(query, con))
                        {
                            cmd.Parameters.AddWithValue("@kms", kms);
                            cmd.Parameters.AddWithValue("@num_lugares", num_lugares);
                            cmd.Parameters.AddWithValue("@matricula", matricula);
                            cmd.Parameters.AddWithValue("@capacidade", capacidade);
                            cmd.Parameters.AddWithValue("@modelo_id", modelo_id);
                            cmd.ExecuteNonQuery();
                        }

                        MessageBox.Show("Autocarro adicionado com sucesso!");

                        showAutocarro.displayAutocarros();

                        this.Hide();
                        showAutocarro.Show();

                    }
                    catch (Exception ex)
                    {
                        MessageBox.Show("Error! " + ex.Message);
                    }
                }
            }
            else
            {
                MessageBox.Show("Dados inseridos inválidos");
            }
        }

        private void dataGridView1_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }
        public void displayModelos()
        {
            using (SqlConnection con = new SqlConnection(conStr))
            {
                try
                {
                    con.Open();
                    string query = "SELECT * FROM EAP.Modelo_autocarro";
                    SqlDataAdapter da = new SqlDataAdapter(query, con);
                    DataTable dt = new DataTable();
                    da.Fill(dt);
                    dataGridView1.DataSource = dt;

                }
                catch (Exception ex)
                {
                    MessageBox.Show("Error! " + ex.Message);
                }
            }
        }

        private void label6_Click(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {
            showAutocarro.displayAutocarros();
            this.Hide();
            showAutocarro.Show();
        }

        private void AddAutocarros_Load(object sender, EventArgs e)
        {

        }
    }


}
