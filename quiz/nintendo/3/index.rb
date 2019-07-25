$num = Integer(gets)
$res = Array.new($num)
for $i in 0...$num
    $res[$i] = Integer(gets)
end

$string = "ZABCDEFGHIJKLMNOPQRSTUVWXY"
for $i in 0...$num
    $argv = $res[$i]
    $trans = ""
    while $argv > 0 do
        $char = $string[$argv%26]
        $trans = $char << $trans
        $argv = ($argv - 1) / 26
    end
    puts $trans
end
