<!DOCTYPE html PUBLIC '-//W3C//DTD XHTML 1.0 Transitional//EN' 'http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd'>
	<html xmlns='http://www.w3.org/1999/xhtml'>
	<head>
	  <meta http-equiv='Content-Type' content='text/html; charset=utf-8' />
	  <title>Test CSV Table Generator</title>
    <link href='https://cdn.datatables.net/1.10.16/css/jquery.dataTables.min.css' rel='stylesheet' type='text/css' />
	  <script src='https://code.jquery.com/jquery-1.12.4.js' type='text/javascript'></script>
	  <script src='https://cdn.datatables.net/1.10.16/js/jquery.dataTables.min.js' type='text/javascript'></script>
	</head>
  <body>
	<script>
			$(document).ready(function(){
                $('#myTable').DataTable();
            });
  </script>
  <br/>
  <table id='myTable' class='display'>
						<thead>
							<tr> 	
								<th>#</th> 
								<th>Category</th>
								<th>Other</th> 
							</tr>
						</thead>
              <td>bit 1</td>
              <td>bit2</td>
    </table>
  </body>
