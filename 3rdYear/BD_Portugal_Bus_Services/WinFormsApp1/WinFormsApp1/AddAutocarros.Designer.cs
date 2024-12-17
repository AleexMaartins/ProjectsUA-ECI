namespace WinFormsApp1
{
    partial class AddAutocarros
    {
        private System.ComponentModel.IContainer components = null;

        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        private void InitializeComponent()
        {
            button2 = new Button();
            button1 = new Button();
            label5 = new Label();
            label4 = new Label();
            label3 = new Label();
            label2 = new Label();
            label1 = new Label();
            textBox4 = new TextBox();
            textBox3 = new TextBox();
            textBox2 = new TextBox();
            textBox1 = new TextBox();
            textBox5 = new TextBox();
            dataGridView1 = new DataGridView();
            label6 = new Label();
            ((System.ComponentModel.ISupportInitialize)dataGridView1).BeginInit();
            SuspendLayout();
            // 
            // button2
            // 
            button2.Location = new Point(12, 17);
            button2.Name = "button2";
            button2.Size = new Size(63, 40);
            button2.TabIndex = 26;
            button2.Text = "Voltar";
            button2.UseVisualStyleBackColor = true;
            button2.Click += button2_Click;
            // 
            // button1
            // 
            button1.Location = new Point(197, 384);
            button1.Name = "button1";
            button1.Size = new Size(324, 29);
            button1.TabIndex = 25;
            button1.Text = "Adicionar Autocarro";
            button1.UseVisualStyleBackColor = true;
            button1.Click += button1_Click;
            // 
            // label5
            // 
            label5.AutoSize = true;
            label5.Location = new Point(573, 84);
            label5.Name = "label5";
            label5.Size = new Size(67, 20);
            label5.TabIndex = 24;
            label5.Text = "modelos";
            // 
            // label4
            // 
            label4.AutoSize = true;
            label4.Location = new Point(174, 248);
            label4.Name = "label4";
            label4.Size = new Size(86, 20);
            label4.TabIndex = 22;
            label4.Text = "capacidade";
            // 
            // label3
            // 
            label3.AutoSize = true;
            label3.Location = new Point(179, 194);
            label3.Name = "label3";
            label3.Size = new Size(71, 20);
            label3.TabIndex = 21;
            label3.Text = "matricula";
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Location = new Point(139, 141);
            label2.Name = "label2";
            label2.Size = new Size(158, 20);
            label2.TabIndex = 20;
            label2.Text = "quantidade de lugares";
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Location = new Point(197, 84);
            label1.Name = "label1";
            label1.Size = new Size(35, 20);
            label1.TabIndex = 19;
            label1.Text = "kms";
            // 
            // textBox4
            // 
            textBox4.Location = new Point(78, 273);
            textBox4.Name = "textBox4";
            textBox4.Size = new Size(279, 27);
            textBox4.TabIndex = 18;
            textBox4.TextChanged += textBox4_TextChanged;
            // 
            // textBox3
            // 
            textBox3.Location = new Point(78, 218);
            textBox3.Name = "textBox3";
            textBox3.Size = new Size(279, 27);
            textBox3.TabIndex = 17;
            textBox3.TextChanged += textBox3_TextChanged;
            // 
            // textBox2
            // 
            textBox2.Location = new Point(78, 164);
            textBox2.Name = "textBox2";
            textBox2.Size = new Size(279, 27);
            textBox2.TabIndex = 16;
            textBox2.TextChanged += textBox2_TextChanged;
            // 
            // textBox1
            // 
            textBox1.Location = new Point(78, 107);
            textBox1.Name = "textBox1";
            textBox1.Size = new Size(279, 27);
            textBox1.TabIndex = 15;
            textBox1.TextChanged += textBox1_TextChanged;
            // 
            // textBox5
            // 
            textBox5.Location = new Point(78, 326);
            textBox5.Name = "textBox5";
            textBox5.Size = new Size(279, 27);
            textBox5.TabIndex = 30;
            textBox5.TextChanged += textBox5_TextChanged;
            // 
            // dataGridView1
            // 
            dataGridView1.ColumnHeadersHeightSizeMode = DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            dataGridView1.Location = new Point(425, 112);
            dataGridView1.Name = "dataGridView1";
            dataGridView1.RowHeadersWidth = 51;
            dataGridView1.Size = new Size(363, 241);
            dataGridView1.TabIndex = 31;
            dataGridView1.CellContentClick += dataGridView1_CellContentClick;
            // 
            // label6
            // 
            label6.AutoSize = true;
            label6.Location = new Point(164, 303);
            label6.Name = "label6";
            label6.Size = new Size(100, 20);
            label6.TabIndex = 32;
            label6.Text = "id do modelo";
            label6.Click += label6_Click;
            // 
            // AddAutocarros
            // 
            AutoScaleDimensions = new SizeF(8F, 20F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(800, 600);
            Controls.Add(label6);
            Controls.Add(dataGridView1);
            Controls.Add(textBox5);
            Controls.Add(button2);
            Controls.Add(button1);
            Controls.Add(label5);
            Controls.Add(label4);
            Controls.Add(label3);
            Controls.Add(label2);
            Controls.Add(label1);
            Controls.Add(textBox4);
            Controls.Add(textBox3);
            Controls.Add(textBox2);
            Controls.Add(textBox1);
            Name = "AddAutocarros";
            Text = "AddAutocarros";
            Load += AddAutocarros_Load;
            ((System.ComponentModel.ISupportInitialize)dataGridView1).EndInit();
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Button button2;
        private Button button1;
        private Label label5;
        private Label label4;
        private Label label3;
        private Label label2;
        private Label label1;
        private TextBox textBox4;
        private TextBox textBox3;
        private TextBox textBox2;
        private TextBox textBox1;

        private TextBox textBox5;
        private DataGridView dataGridView1;
        private Label label6;
    }
}
