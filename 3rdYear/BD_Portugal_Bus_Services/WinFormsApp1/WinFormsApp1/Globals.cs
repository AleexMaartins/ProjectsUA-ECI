using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace WinFormsApp1
{
    public static class Globals
    {
        private static string dbServer = "tcp:mednat.ieeta.pt\\SQLSERVER,8101;TrustServerCertificate=True";

        private static string dbName = "p2g2";
        private static string userName = "p2g2";
        private static string userPass = "-1884967622@BDalexcheiivan";

        public static string strConn = "Data Source = " + dbServer + " ;" + "Initial Catalog = " + dbName + "; uid = " + userName + ";" + "password = " + userPass;

    }
}
