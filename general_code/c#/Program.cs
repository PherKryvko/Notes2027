/*
Split and join: Take " ada, linus ,,grace ", split it on commas, drop the blanks and extra spaces, then print the names joined with " | ".
Null handling: Declare string? nickname = null; and print none if it’s null or blank, without crashing.
Formatting: Print a decimal price of 1234.5m as £1,234.50, and today’s date as 2026-11-17.
StringBuilder: Build a three-line report (Line 1, Line 2, Line 3) with StringBuilder, then print it.
Case-insensitive check: Check whether " YES " matches "yes", ignoring case and spaces, and print true or false.
Constants, types and scope: Declare const int MaxNames = 3;, use var for a value you assign later in a block, and print the value after the block.
*/
using System.Text;

string names_ = " ada, linus ,,grace ";
names_ = names_.Trim();
string[] collection = names_.Split(',', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries);
string names__ = string.Join(" | ", collection);
Console.WriteLine(names__);


string? nick = null;

if (string.IsNullOrWhiteSpace(nick))
{
    Console.WriteLine("none");
}


decimal cost = 1234.5m;
//as £1,234.50, and today’s date as 2026-11-17.
Console.WriteLine($"£{cost:N2}");
Console.WriteLine($"{DateTime.Today:yyyy-MM-dd}");


var sb = new StringBuilder();

for (int i = 1; i < 4; i++)
{
    sb.AppendLine("Line " + i);
}

string newSB = sb.ToString();
Console.WriteLine(newSB);


//Case-insensitive check: Check whether " YES " matches "yes", ignoring case and spaces, and print true or false.

string yes = "  YES  ";

if(string.Equals(yes.Trim(), "yes", StringComparison.OrdinalIgnoreCase))
{
    Console.WriteLine("True");
}
else
{
    Console.WriteLine("False");
}


//Constants, types and scope: Declare const int MaxNames = 3;, use var for a value you assign later in a block, and print the value after the block.
const int MaxNames = 3;
var noot = 1;

if(noot == 1)
{
    noot = 3;
}

Console.Write(noot);














/*
Write a Split that turns "a, b,c ,,d" into ["a", "b", "c", "d"].
*/
string abcd = "a, b,c ,,d";
string[] split = abcd.Split(',', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries);


string t = "hello"; 
Console.WriteLine(t[1..^1]); //# What prints? //This prints not first index of h, but goes from e to the end ^1

//What prints for Console.WriteLine(@"D:\new\test");, and what would "D:\new\test" print instead?
Console.WriteLine(@"D:\new\test"); //No clue but verbatim means the backslashes are kept for the directory stuff, the other one doesn't have it so it causes new lines to occur

/*
   Console.WriteLine($"[{"hi",-6}]");
   Console.WriteLine($"{12345.678:N1}");
*/
//Moves hi by -6 indentation, N2 rounds to 2, so maybe N1 rounds to 1 .... >there is also thus one
Console.WriteLine($"{DateTime.Today:dd-MM-yyyy}");



/*
Take " Alice ; bob ;; CHARLIE ", split on ;, 
trim each piece, and drop empty entries. Print each name in upper case, one per line, as NAME (length).
*/
string namesAgain = " Alice ; bob ;; CHARLIE ";
string[] DDDDD = namesAgain.Split(';', StringSplitOptions.TrimEntries | StringSplitOptions.RemoveEmptyEntries);

foreach(string item in DDDDD)
{
    Console.WriteLine($"{item.ToUpper()} {item.Length}");
}

/*
Use a StringBuilder to build a report with one line per number from 1 to 5, 
each line reading Row i: i squared is N. Then print the whole report.
*/
StringBuilder sbNEW = new StringBuilder();

for(int i = 1; i <= 5; i++){
    sbNEW.Append($"Row i: {i} squared is {i*i}").AppendLine();
}
string appended = sbNEW.ToString();
Console.WriteLine(appended);

/*
You have string[] allowed = { "start", "stop" };. 
Take the user input " START ", trim it, and check it against the allowed list ignoring case. Print ok if it matches, otherwise unknown.
*/
string[] allowed = { "start", "stop" };
string userInput = " START ";
userInput = userInput.Trim();

if (string.Equals(allowed[0], userInput, StringComparison.OrdinalIgnoreCase)){
    Console.Write("ok");
}else{
    Console.Write("unknown");
}

/*
For a decimal price of 1234.5m and a name "Tea", 
print one line with the name left-aligned in 12 characters, then the price right-aligned in 10 characters, formatted with two decimal places and a £ sign.
*/
decimal cosssst = 1234.5m;
string cup = "Tea";

Console.WriteLine($"\n{cup, -12} £{cosssst, 10:N2}");