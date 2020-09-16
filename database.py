import mysql.connector as msql


def getcolor(guild):
    mydb = msql.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)
    cursor = mydb.cursor()
    cursor.execute(f"SELECT color FROM colors WHERE guildid = '{guild}' ")
    result = cursor.fetchone()
    rgb = tuple(int(result[0][i:i + 2], 16) for i in (0, 2, 4))
    cursor.close()
    mydb.close()
    return rgb


def get_prefix(guild):
    mydb = msql.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)
    cursor = mydb.cursor()
    cursor.execute(
        f"SELECT * FROM prefix WHERE guildid = '{guild}'")
    result = cursor.fetchone()
    cursor.close()
    mydb.close()
    return result[1]
