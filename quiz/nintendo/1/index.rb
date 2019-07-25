while $origin = gets
    $nums = $origin.scan(/\d+/)
    $res = 0
    $nums.each do |num|
        $res += Integer(num)
    end
    puts $res
end
