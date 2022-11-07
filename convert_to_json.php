<?php
    // sources: https://stackoverflow.com/questions/2467945/how-to-generate-json-data-with-php
    //          https://www.kodingmadesimple.com/2015/01/convert-mysql-to-json-using-php.html

    // export the SQL SELECT queries into JSON format to perform data manipulation using NoSQL

    //open connection to mysql db
    $connection = mysqli_connect("localhost:3306","root","ViolinOkTree5678!","sakila") or die("Error " . mysqli_error($connection));

    //fetch table rows from mysql db
    //$sql = "SELECT * from film";
    //$sql = "SELECT * from actor";
    //$sql = "SELECT * from address";
    //$sql = "SELECT * from city";
    //$sql = "SELECT * from country";
    //$sql = "SELECT * from customer";
    //$sql = "SELECT * from film_actor";
    //$sql = "SELECT * from film_category";
    //$sql = "SELECT * from film_text";
    //$sql = "SELECT * from inventory";
    //$sql = "SELECT * from language";
    //$sql = "SELECT * from payment";
    //$sql = "SELECT * from rental";
    //$sql = "SELECT * from store";
    $sql = "SELECT * from staff";
    $result = mysqli_query($connection, $sql) or die("Error in Selecting " . mysqli_error($connection));

    //create an array
    $my_array = array();
    while($row =mysqli_fetch_assoc($result))
    {
        $my_array[] = $row;
    }
    echo json_encode($my_array);
    file_put_contents('./data/staff.json', json_encode($my_array));

    //close the db connection
    mysqli_close($connection);
?>