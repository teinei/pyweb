<?php
require_once "pdo.php";
session_start();

$input_begin_year=2017;
$input_begin_month=1;
$input_begin_day=1;
//
$input_end_year=2020;
$input_end_month=1;
$input_end_day=1;

//input begin date setter
if(isset($_POST['begin_year'])){
	$input_begin_year=$_POST['begin_year'];
}
if(isset($_POST['begin_month'])){
	$input_begin_month=$_POST['begin_month'];
}
if(isset($_POST['begin_day'])){
	$input_begin_day=$_POST['begin_day'];
}
$input_begin_date=$input_begin_year."-".
	$input_begin_month."-".$input_begin_day;
//echo "$input_begin_date";
//input begin date setter fin

//input end date setter by post form
if(isset($_POST['end_year'])){
	$input_end_year=$_POST['end_year'];
}
if(isset($_POST['end_month'])){
	$input_end_month=$_POST['end_month'];
}
if(isset($_POST['end_day'])){
	$input_end_day=$_POST['end_day'];
}
$input_end_date=$input_end_year."-".
	$input_end_month."-".$input_end_day;
//input end date setter by post form closed

//db column variables
$sum_id=0;
$open_date=0;
$class_name=0;
$main_teacher=0;
$co_teacher=0;
$average=0;
$text1=0;
$text2=0;
$text3=0;
//db column variables
?>
<html>
<head>
<meta content="text/html; charset=utf-8">
</head>
<body>
<a href="../crud-surveys/index.php">back to surveys index</a><br>
<br>
<form method="post">
<?php
/*
	<p>
	begin: 
	year
		<input type="text" name="begin_year"
		value="<?= $_POST['begin_year'] ?>">
	month
		<input type="text" name="begin_month"
		value="<?= $_POST['begin_month'] ?>">
	day
		<input type="text" name="begin_day"
		value="<?= $_POST['begin_day'] ?>">
	</p>
	<p>
	end: 
	year
		<input type="text" name="end_year"
		value="<?= $_POST['end_year'] ?>">
	month
		<input type="text" name="end_month"
		value="<?= $_POST['end_month'] ?>">
	day
		<input type="text" name="end_day"
		value="<?= $_POST['end_day'] ?>">
	</p>
	<p><input type="submit" value="Start Queue"/>
</form>
*/
?>
	<p>
	begin: 
	year
		<input type="text" name="begin_year" size="4"
		value="<?=$input_begin_year?>">
	month
		<input type="text" name="begin_month" size="2"
		value="<?= $input_begin_month ?>">
	day
		<input type="text" name="begin_day" size="2"
		value="<?= $input_begin_day ?>">
	</p>
	<p>
	end: 
	year
		<input type="text" name="end_year" size="4"
		value="<?= $input_end_year ?>">
	month
		<input type="text" name="end_month" size="2"
		value="<?= $input_end_month ?>">
	day
		<input type="text" name="end_day" size="2"
		value="<?= $input_end_day ?>">
	</p>
	<p><input type="submit" value="Start Queue"/>
</form>

<?php
function survey_sums_by_date($input_begin_date_arg,$input_end_date_arg){
	require "pdo.php";
	//
	/*
	$sql = "UPDATE `user` SET `password`=:password WHERE `user_id`=:userId";  
	$stmt = $dbh->prepare($sql);  
	$stmt->execute(array(':userId'=>'7', ':password'=>'4607e782c4d86fd5364d7e4508bb10d9'));  
	echo $stmt->rowCount();
	*/
	$sql="SELECT 
		sum_id,
		open_date,
		class_name,
		main_teacher,co_teacher,
		average,
		text1,text2,text3
	FROM
		survey_sum
	WHERE 
		survey_sum.open_date <= :input_end_date 
	AND
		survey_sum.open_date >= :input_begin_date
	";
	$stmt = $pdo->prepare($sql);
	$stmt->execute(array(
		':input_begin_date' => $input_begin_date_arg,
		':input_end_date' => $input_end_date_arg
	));
	//

	//table header open
	echo "<table border='1'>";
	echo "<tr>";
	echo "<td>sum_id</td>";
	echo "<td>class_name</td>";
	echo "<td>open_date</td>";
	echo "<td>main_teacher</td> <td>co_teacher</td>";
	echo "<td>average</td>";
	echo "<td> text1</td><td>text2</td><td>text3</td>";
	echo "<td></td>";
	echo "</tr>";
	//table header close
	
	while ( $row = $stmt->fetch(PDO::FETCH_ASSOC)) {
		//echo "<br>";
		//var_dump($row);
		//	
		$sum_id=htmlentities($row['sum_id']);
		//
		$open_date=$row['open_date'];
		//
		$class_name=$row['class_name'];
		$main_teacher=$row['main_teacher'];
		$co_teacher=$row['co_teacher'];
		$average=$row['average'];
		$text1=$row['text1'];
		$text2=$row['text2'];
		$text3=$row['text3'];

		echo ("<tr><td>");//row start
		echo "$sum_id";
		echo("</td>");
		//		
		echo("<td>");
		echo "$class_name";//alter key name
		echo("</td>");
			//
		echo("<td>");
		echo "$open_date";//alter key name
		echo("</td>");
		//
		echo("<td>");
		echo "$main_teacher";
		echo("</td>");
		
		echo("<td>");
		echo "$co_teacher";
		echo("</td>");
	//
		echo("<td>");
		echo "$average";
		echo("</td>");
		
		echo("<td>");
		echo "$text1";
		echo("</td>");
	
		echo("<td>");
		echo "$text2";
		echo("</td>");
	//
		echo("<td>");
		echo "$text3";
		echo("</td>");

		echo("<td>");
		echo('<a href="edit.php?sum_id='.$sum_id.'">Edit</a> / ');
		echo('<a href="delete.php?sum_id='.$sum_id.'">Delete</a>');
		echo("</td></tr>\n");	
	}
	echo "</table>";
	//
	//
}

//
survey_sums_by_date($input_begin_date,$input_end_date);
echo "<br><br><br>";
?>