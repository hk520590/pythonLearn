import ConnectSql
import ReadWriteFile
import sys

def main():
    ReadWriteFile.OpenAndWriteTxt()
    #ConnectSql.ConnectSql()
    ConnectSql.backupSql()

if __name__ == "__main__":
    sys.exit(main())
