while $argvs = gets
    $c1, $c2 = $argvs.split
    $c1Arr = $c1.split('/')
    $c2Arr = $c2.split('/')
    $hp1 = Integer($c1Arr[0])
    $hp2 = Integer($c2Arr[0])

    $at1 = Integer($c1Arr[1])
    $at2 = Integer($c2Arr[1])

    $def1 = Integer($c1Arr[2])
    $def2 = Integer($c2Arr[2])

    # effective attack
    $eff_att1 = $at1-$def2
    $eff_att2 = $at2-$def1

    if $eff_att1 < 1
        if $eff_att2 < 1
            #勝敗が決定しない場合
            if $hp1 > $hp2
                puts "Win 0"
            elsif $hp1 < $hp2
                puts "Lose 0"
            else
                puts "Draw 0"
            end
        else
            $time = ($hp1-1) / $eff_att2 + 1
            puts "Lose #{$time}"
        end
    else
        if $eff_att2 < 1
            $time = ($hp2-1) / $eff_att1 + 1
            puts "Win #{$time}"
        else
            $time1 = ($hp2-1) / $eff_att1 + 1
            $time2 = ($hp1-1) / $eff_att2 + 1
            if $time1 > $time2
                #lose
                puts "Lose #{$time2}"
            elsif $time1 < $time2
                puts "Win #{$time1}"
            else
                #双方のHPが同じターンで0以下となった場合、最終的なHPがより高いキャラクターが勝利する。最終的なHPが同じ場合は引き分けとする。
                $resHP1 = $hp1 - $time2*$eff_att2
                $resHP2 = $hp2 - $time1*$eff_att1
                if $resHP1 > $resHP2
                    puts "Win #{$time1}"
                elsif $resHP1 < $resHP2
                    puts "Lose #{$time2}"
                else
                    puts "Draw #{$time1}"
                end
            end
        end
    end
end
