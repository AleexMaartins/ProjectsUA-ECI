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

namespace WinFormsApp1
{
    public partial class ShowPeople : Form
    {
        private AddPassageiro addPassageiro;
        private AddCondutor addCondutor;
        private menu menu;
        //private string conStr = "Data Source=DESKTOP-RGVE259;Initial Catalog=EAP;Integrated Security=True;TrustServerCertificate=True";
        private string conStr = Globals.strConn;

        public ShowPeople(menu menu)
        {
            InitializeComponent();
            displayPessoas();
            addPassageiro = new AddPassageiro(this);
            addCondutor = new AddCondutor(this);
            this.menu = menu;
        }

        private void dataGridView1_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }

        public void displayPessoas()
        {
            using (SqlConnection con = new SqlConnection(conStr))
            {
                try
                {
                    con.Open();
                    string query = @"
                                    SELECT p.*, 
                                           CASE 
                                               WHEN c.pessoa_id IS NOT NULL THEN 'Condutor'
                                               WHEN pa.pessoa_id IS NOT NULL THEN 'Passageiro'
                                               ELSE 'Unknown'
                                           END as Type,
                                           c.carta_conducao,  -- Assuming this field is in the Condutor table
                                           pa.faixa_etaria       -- Assuming this field is in the Passageiro table
                                    FROM EAP.Pessoa p 
                                    LEFT JOIN EAP.Condutor c ON p.id = c.pessoa_id 
                                    LEFT JOIN EAP.Passageiro pa ON p.id = pa.pessoa_id";
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

        private void button1_Click(object sender, EventArgs e)
        {
            addPassageiro.Show();
            this.Hide();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            addCondutor.Show();
            this.Hide();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            menu.Show();
            this.Hide();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            // Get the id of the selected person
            string idText = textBox1.Text;
            Console.WriteLine("ID Text: " + idText); // Print the ID text

            if (int.TryParse(idText, out int id))
            {
                using (SqlConnection con = new SqlConnection(conStr))
                {
                    try
                    {
                        con.Open();
                        string query = "DELETE FROM EAP.Pessoa WHERE id = @id";

                        using (SqlCommand cmd = new SqlCommand(query, con))
                        {
                            cmd.Parameters.AddWithValue("@id", id);
                            int rowsAffected = cmd.ExecuteNonQuery();

                            if (rowsAffected > 0)
                            {
                                MessageBox.Show("Pessoa deleted successfully!");

                                // Refresh the data grid view
                                displayPessoas();
                            }
                            else
                            {
                                MessageBox.Show("No person with the given ID was found.");
                            }
                        }
                    }
                    catch (Exception ex)
                    {
                        MessageBox.Show("Error! " + ex.Message);
                    }
                }
            }
            else
            {
                MessageBox.Show("Invalid ID.");
            }
        }

        

        private void textBox3_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {
            if (!int.TryParse(textBox1.Text, out _))
            {
                // The text in textBox1 is not a valid integer
                MessageBox.Show("Please enter a valid ID.");
            }
        }

        private void textBox2_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox1_TextChanged_1(object sender, EventArgs e)
        {

        }

        private void label4_Click(object sender, EventArgs e)
        {

        }

        private void textBox4_TextChanged(object sender, EventArgs e)
        {

        }

       

        private void textBox5_TextChanged(object sender, EventArgs e)
        {

        }
    }

}
