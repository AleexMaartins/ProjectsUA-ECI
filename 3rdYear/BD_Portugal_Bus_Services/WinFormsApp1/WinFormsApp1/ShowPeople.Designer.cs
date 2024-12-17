namespace WinFormsApp1
{
    partial class ShowPeople
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }



        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            dataGridView1 = new DataGridView();
            button1 = new Button();
            button2 = new Button();
            button3 = new Button();
            buttonDelete_Click = new Button();
            label1 = new Label();
            textBox1 = new TextBox();
            ((System.ComponentModel.ISupportInitialize)dataGridView1).BeginInit();
            SuspendLayout();
            // 
            // dataGridView1
            // 
            dataGridView1.ColumnHeadersHeightSizeMode = DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            dataGridView1.Location = new Point(12, 55);
            dataGridView1.Name = "dataGridView1";
            dataGridView1.RowHeadersWidth = 51;
            dataGridView1.Size = new Size(1215, 205);
            dataGridView1.TabIndex = 0;
            dataGridView1.CellContentClick += dataGridView1_CellContentClick;
            // 
            // button1
            // 
            button1.Location = new Point(432, 278);
            button1.Name = "button1";
            button1.Size = new Size(170, 47);
            button1.TabIndex = 1;
            button1.Text = "Adicionar Passageiro";
            button1.UseVisualStyleBackColor = true;
            button1.Click += button1_Click;
            // 
            // button2
            // 
            button2.Location = new Point(639, 278);
            button2.Name = "button2";
            button2.Size = new Size(170, 47);
            button2.TabIndex = 2;
            button2.Text = "Adicionar Condutor";
            button2.UseVisualStyleBackColor = true;
            button2.Click += button2_Click;
            // 
            // button3
            // 
            button3.Location = new Point(12, 12);
            button3.Name = "button3";
            button3.Size = new Size(157, 37);
            button3.TabIndex = 3;
            button3.Text = "Voltar ao menu";
            button3.UseVisualStyleBackColor = true;
            button3.Click += button3_Click;
            // 
            // buttonDelete_Click
            // 
            buttonDelete_Click.Location = new Point(563, 397);
            buttonDelete_Click.Name = "buttonDelete_Click";
            buttonDelete_Click.Size = new Size(125, 37);
            buttonDelete_Click.TabIndex = 4;
            buttonDelete_Click.Text = "Apagar Pessoa";
            buttonDelete_Click.UseVisualStyleBackColor = true;
            buttonDelete_Click.Click += button4_Click;
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Location = new Point(584, 341);
            label1.Name = "label1";
            label1.Size = new Size(70, 20);
            label1.TabIndex = 7;
            label1.Text = "Pessoa Id";
            // 
            // textBox1
            // 
            textBox1.Location = new Point(563, 364);
            textBox1.Name = "textBox1";
            textBox1.Size = new Size(125, 27);
            textBox1.TabIndex = 12;
            textBox1.TextChanged += textBox1_TextChanged_1;
            // 
            // ShowPeople
            // 
            AutoScaleDimensions = new SizeF(8F, 20F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(1240, 450);
            Controls.Add(label1);
            Controls.Add(buttonDelete_Click);
            Controls.Add(button3);
            Controls.Add(button2);
            Controls.Add(button1);
            Controls.Add(dataGridView1);
            Controls.Add(textBox1);
            Name = "ShowPeople";
            Text = "ShowPeople";
            ((System.ComponentModel.ISupportInitialize)dataGridView1).EndInit();
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private DataGridView dataGridView1;
        private Button button1;
        private Button button2;
        private Button button3;
        private Button buttonDelete_Click;
        private Label label1;
        private TextBox textBox3;
        private TextBox textBox1;
    }
}