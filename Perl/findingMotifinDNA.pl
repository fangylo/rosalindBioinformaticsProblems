#!/usr/bin/env perl
use warnings;
use strict; 
use List::Util qw(max);

# sub countnmstr
# {
    # my ($string, $substr) = @_;
    # return scalar( () = $string =~ /(?=\Q$substr\E)/g );
# }

# my $count = countnmstr("aaa","aa");

# print "$count\n";

# # my $result = findMaxPalindrome();
# # print $result;

my @matches;
while ( 'aaabaa' =~ /'aa'/g  )
{
    push @matches, $1;
}

print @matches;