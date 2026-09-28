<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Employee table</title>
	<style>
		body {
			width: 750px;
			margin: 0 auto;
		}
		table {
			border-collapse: collapse;
			border: 1px solid black;
			margin: 20px;
		}
		caption {
			font-size: 150%;
			font-weight: bold;
			padding-bottom: .5em;
		}
		thead, tfoot {
			background-color: yellow;
		}
		tfoot {
			font-weight: bold;
		}
		th, td {
			border: 1px solid black;
			padding: .2em 1em .2em .5em;
			text-align: left;
			vertical-align: middle;
		}
		.right {
			text-align: right;
		}
		.top {
			vertical-align: top;
		}
		tbody tr:nth-child(even) td {
			background-color: yellow;
		}
	</style>
</head>

<body>
<table>
	<caption>Employee Table</caption>
	<thead>
		<tr>
			<th>Department</th>
			<th>Name</th>
			<th>E-mail</th>
			<th class="right">Years of Service</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<th class="top" rowspan="3">Editorial</th>
			<td>Joel Murach</td>
			<td>joelmurach@yahoo.com</td>
			<td class="right">22</td>
		</tr>
		<tr>
			<td>Anne Boehm</td>
			<td>anne@murach.com</td>
			<td class="right">34</td>
		</tr>
		<tr>
			<td>Zak Ruvalcaba</td>
			<td>zak@modulemedia.com</td>
			<td class="right">4</td>
		</tr>
		<tr>
			<th class="top" rowspan="2">Marketing</th>
			<td>Judy Taylor</td>
			<td>judy@murach.com</td>
			<td class="right">39</td>
		</tr>
		<tr>
			<td>Cyndi Vasquez</td>
			<td>cyndi@murach.com</td>
			<td class="right">10</td>
		</tr>
		<tr>
			<th class="top" rowspan="2">Customer Service</th>
			<td>Kelly Slivkoff</td>
			<td>kelly@murach.com</td>
			<td class="right">25</td>
		</tr>
		<tr>
			<td>Juliette Baylon</td>
			<td>juliette@murach.com</td>
			<td class="right">1</td>
		</tr>
	</tbody>
	<tfoot>
		<tr>
			<th class="right" colspan="3">Total Years of Service</th>
			<td class="right">105</td>
		</tr>
	</tfoot>
</table>
</body>
</html>
