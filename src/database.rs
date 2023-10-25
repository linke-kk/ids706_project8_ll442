extern crate rusqlite;

use rusqlite::{params, Connection, Result};

fn connect_to_database(db: &str) -> Result<Connection> {
    Connection::open(db)
}

fn create_table(conn: &Connection, query_creation: &str) -> Result<()> {
    conn.execute(query_creation, [])?;
    Ok(())
}

fn insert_data(conn: &Connection, sql_insertion: &str, i1: &str, i2: i64, i3: &str) -> Result<()> {
    conn.execute(sql_insertion, params![i1, i2, i3])?;
    Ok(())
}

fn read_data(conn: &Connection, sql_read: &str, input_read: &str) -> Result<()> {
    let mut stmt = conn.prepare(sql_read)?;
    let rows = stmt.query_map(params![input_read], |row| {
        let name: String = row.get(1)?;
        let stock: i64 = row.get(2)?;
        let comment: String = row.get(3)?;
        Ok((name, stock, comment))
    })?;

    for row in rows {
        println!("{:?}", row?);
    }

    Ok(())
}

fn update_data(conn: &Connection, query_update: &str, stock: i64, name: &str) -> Result<()> {
    conn.execute(query_update, params![stock, name])?;
    Ok(())
}

fn delete_data(conn: &Connection, sql_delete: &str, name2: &str) -> Result<()> {
    conn.execute(sql_delete, params![name2])?;
    Ok(())
}

fn count_book_by_stock(conn: &Connection, stock: i64) -> Result<i64> {
    conn.query_row(
        "SELECT COUNT(*) FROM books WHERE stock=?",
        params![stock],
        |row| row.get(0),
    )
}

fn fetch_books_ordered_by_name(conn: &Connection) -> Result<Vec<(i64, String, i64, String)>> {
    let mut stmt = conn.prepare("SELECT * FROM books ORDER BY name")?;
    let rows = stmt.query_map([], |row| {
        Ok((row.get(0)?, row.get(1)?, row.get(2)?, row.get(3)?))
    })?;

    Ok(rows.map(|row| row.unwrap()).collect())
}

fn main() -> Result<()> {
    let db_name = "book.db";
    let conn = connect_to_database(db_name)?;

    let query_creation = "
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            stock INTEGER NOT NULL,
            comment TEXT
        )
    ";
    create_table(&conn, query_creation)?;

    let query_insertion = "INSERT INTO books (name, stock, comment) VALUES (?1, ?2, ?3)";
    insert_data(
        &conn,
        query_insertion,
        "Red Chamber",
        30,
        "Uncopiable Love Story",
    )?;
    insert_data(
        &conn,
        query_insertion,
        "Educated",
        35,
        "Meaning of Education",
    )?;

    let query_read = "SELECT * FROM books WHERE name=?1";
    let input_read = "Red Chamber";
    read_data(&conn, query_read, input_read)?;

    let query_update = "UPDATE books SET stock=?1 WHERE name=?2";
    let stock = 25;
    let name = "Red Chamber";
    update_data(&conn, query_update, stock, name)?;

    println!("{:?}", count_book_by_stock(&conn, 35)?);
    for row in fetch_books_ordered_by_name(&conn)? {
        println!("{:?}", row);
    }

    let query_deletion = "DELETE FROM books WHERE name=?1";
    let name2 = "Red Chamber";
    let name3 = "Educated";
    delete_data(&conn, query_deletion, name2)?;
    delete_data(&conn, query_deletion, name3)?;

    Ok(())
}
