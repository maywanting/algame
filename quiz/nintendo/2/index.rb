while $args = gets
    $strings = $args.split
    $res = Hash.new
    $strings.each do |strTemp|
        $res[strTemp] = 1
    end
    puts $res.keys.join(" ")
end
