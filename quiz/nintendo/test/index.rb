$num = Integer(gets);
$res = Array.new($num);
for $i in 0...$num
    $res[$i] = gets;
end

for $i in 0...$num
    puts "Hello!, #{$res[$i]}";
end
