namespace WinFormsApp1
{
    partial class ComprarBilhete
    {
        private System.ComponentModel.IContainer components = null;
        private TextBox textBox1;
        private TextBox textBox2;
        private Label label1;
        private Label label2;
        private Button btnSearch;
        private DataGridView dataGridView1;

        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        private void InitializeComponent()
        {
            textBox1 = new TextBox();
            textBox2 = new TextBox();
            label1 = new Label();
            label2 = new Label();
            btnSearch = new Button();
            dataGridView1 = new DataGridView();
            button2 = new Button();
            textBox5 = new TextBox();
            label5 = new Label();
            textBox6 = new TextBox();
            label6 = new Label();
            textBox7 = new TextBox();
            label7 = new Label();
            textBox8 = new TextBox();
            label8 = new Label();
            dataGridView2 = new DataGridView();
            button1 = new Button();
            ((System.ComponentModel.ISupportInitialize)dataGridView1).BeginInit();
            ((System.ComponentModel.ISupportInitialize)dataGridView2).BeginInit();
            SuspendLayout();
            // 
            // textBox1
            // 
            textBox1.Location = new Point(126, 68);
            textBox1.Name = "textBox1";
            textBox1.Size = new Size(200, 27);
            textBox1.TabIndex = 0;
            // 
            // textBox2
            // 
            textBox2.Location = new Point(126, 108);
            textBox2.Name = "textBox2";
            textBox2.Size = new Size(200, 27);
            textBox2.TabIndex = 1;
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Location = new Point(56, 68);
            label1.Name = "label1";
            label1.Size = new Size(62, 20);
            label1.TabIndex = 2;
            label1.Text = "Origem:";
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Location = new Point(56, 108);
            label2.Name = "label2";
            label2.Size = new Size(63, 20);
            label2.TabIndex = 3;
            label2.Text = "Destino:";
            // 
            // btnSearch
            // 
            btnSearch.Location = new Point(180, 151);
            btnSearch.Name = "btnSearch";
            btnSearch.Size = new Size(87, 34);
            btnSearch.TabIndex = 4;
            btnSearch.Text = "Procurar";
            btnSearch.UseVisualStyleBackColor = true;
            btnSearch.Click += btnSearch_Click;
            // 
            // dataGridView1
            // 
            dataGridView1.ColumnHeadersHeightSizeMode = DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            dataGridView1.Location = new Point(44, 208);
            dataGridView1.Name = "dataGridView1";
            dataGridView1.RowHeadersWidth = 51;
            dataGridView1.Size = new Size(575, 207);
            dataGridView1.TabIndex = 5;
            // 
            // button2
            // 
            button2.Location = new Point(822, 168);
            button2.Name = "button2";
            button2.Size = new Size(136, 29);
            button2.TabIndex = 19;
            button2.Text = "comprar bilhete";
            button2.UseVisualStyleBackColor = true;
            button2.Click += button2_Click;
            // 
            // textBox5
            // 
            textBox5.Location = new Point(919, 131);
            textBox5.Name = "textBox5";
            textBox5.Size = new Size(166, 27);
            textBox5.TabIndex = 18;
            // 
            // label5
            // 
            label5.AutoSize = true;
            label5.Location = new Point(970, 108);
            label5.Name = "label5";
            label5.Size = new Size(58, 20);
            label5.TabIndex = 17;
            label5.Text = "destino";
            // 
            // textBox6
            // 
            textBox6.Location = new Point(919, 68);
            textBox6.Name = "textBox6";
            textBox6.Size = new Size(166, 27);
            textBox6.TabIndex = 16;
            // 
            // label6
            // 
            label6.AutoSize = true;
            label6.Location = new Point(970, 45);
            label6.Name = "label6";
            label6.Size = new Size(57, 20);
            label6.TabIndex = 15;
            label6.Text = "origem";
            // 
            // textBox7
            // 
            textBox7.Location = new Point(705, 131);
            textBox7.Name = "textBox7";
            textBox7.Size = new Size(166, 27);
            textBox7.TabIndex = 14;
            // 
            // label7
            // 
            label7.AutoSize = true;
            label7.Location = new Point(745, 109);
            label7.Name = "label7";
            label7.Size = new Size(77, 20);
            label7.TabIndex = 13;
            label7.Text = "viagem_id";
            // 
            // textBox8
            // 
            textBox8.Location = new Point(705, 68);
            textBox8.Name = "textBox8";
            textBox8.Size = new Size(166, 27);
            textBox8.TabIndex = 12;
            // 
            // label8
            // 
            label8.AutoSize = true;
            label8.Location = new Point(734, 45);
            label8.Name = "label8";
            label8.Size = new Size(100, 20);
            label8.TabIndex = 11;
            label8.Text = "passageiro_id";
            // 
            // dataGridView2
            // 
            dataGridView2.ColumnHeadersHeightSizeMode = DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            dataGridView2.Location = new Point(648, 208);
            dataGridView2.Name = "dataGridView2";
            dataGridView2.RowHeadersWidth = 51;
            dataGridView2.Size = new Size(629, 207);
            dataGridView2.TabIndex = 20;
            dataGridView2.CellContentClick += dataGridView2_CellContentClick;
            // 
            // button1
            // 
            button1.Location = new Point(12, 12);
            button1.Name = "button1";
            button1.Size = new Size(63, 40);
            button1.TabIndex = 21;
            button1.Text = "Voltar";
            button1.UseVisualStyleBackColor = true;
            button1.Click += button1_Click;
            // 
            // ComprarBilhete
            // 
            ClientSize = new Size(1289, 450);
            Controls.Add(button1);
            Controls.Add(dataGridView2);
            Controls.Add(button2);
            Controls.Add(textBox5);
            Controls.Add(label5);
            Controls.Add(textBox6);
            Controls.Add(label6);
            Controls.Add(textBox7);
            Controls.Add(label7);
            Controls.Add(textBox8);
            Controls.Add(label8);
            Controls.Add(dataGridView1);
            Controls.Add(btnSearch);
            Controls.Add(label2);
            Controls.Add(label1);
            Controls.Add(textBox2);
            Controls.Add(textBox1);
            Name = "ComprarBilhete";
            Text = "Comprar Bilhete";
            Load += ComprarBilhete_Load;
            ((System.ComponentModel.ISupportInitialize)dataGridView1).EndInit();
            ((System.ComponentModel.ISupportInitialize)dataGridView2).EndInit();
            ResumeLayout(false);
            PerformLayout();
        }

        private Button button2;
        private TextBox textBox5;
        private Label label5;
        private TextBox textBox6;
        private Label label6;
        private TextBox textBox7;
        private Label label7;
        private TextBox textBox8;
        private Label label8;
        private DataGridView dataGridView2;
        private Button button1;
    }
}
