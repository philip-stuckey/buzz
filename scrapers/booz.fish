function booz --argument infile
	set content (xmllint --html --xpath "//meta[@name='description']/@content" $infile | cut -d '"' -f2)
	set outfile examples/(basename $infile)
	echo $content > $outfile
end
