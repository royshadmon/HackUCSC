function jj_readcsv($filename, $header=false) {
$handle = fopen($filename, "r");
echo '<table>';
//display header row if true
if ($header) {
    $csvcontents = fgetcsv($handle);
    echo '<tr>';
    foreach ($csvcontents as $headercolumn) {
        echo "<th>$headercolumn</th>";
    }
    echo '</tr>';
}
// displaying contents
while ($csvcontents = fgetcsv($handle)) {
    echo '<tr>';
    foreach ($csvcontents as $column) {
        echo "<td>$column</td>";
    }
    echo '</tr>';
}
echo '</table>';
fclose($handle);
}