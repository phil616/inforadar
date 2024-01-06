from rpyc import connect
if __name__ == "__main__":
    conn = connect(host="127.0.0.1", port=9999)
    print(conn.root)
    print(conn.root.constant_value)
    print(conn.root.get_info())

    print(conn.root.network_get({"url":"https://www.baidu.com"}))
