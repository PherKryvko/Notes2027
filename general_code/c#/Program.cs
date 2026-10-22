//////////////////////////////////STRING BUILDER
using System.Text;

var sb = new StringBuilder();

for(int i = 0; i < 3; i++){
    sb.Append($"NEW LINE").AppendLine();
}

string builtSB = sb.ToString();
Console.WriteLine(builtSB);


//////////////////////////////////SPLIT JOIN
string names = "apple, banana ,cherry";
string[] pieces = names.Split(',', StringSplitOptions.TrimEntries | StringSplitOptions.RemoveEmptyEntries);
string collected = string.Join(" | ", pieces);
Console.WriteLine(collected);

if(collected.StartsWith("E")){
    
}


/////////////Formatting
string name = " eeee ee e eee";
decimal price = 1234.5m;
Console.WriteLine($"£{price:N2}");                 // £1,234.50
Console.WriteLine($"{DateTime.Today:yyyy-MM-dd}"); // e.g. 2026-10-22
Console.WriteLine($"[{name,-10}]");                // left-align in 10 characters
Console.WriteLine($"[{name,10}]");                 // right-align in 10 characters


///MISC
string a = "E";
string b = "EE";

Console.WriteLine(name[1..3]); 
Console.WriteLine(name[^1]);
string.Equals(a, b, StringComparison.OrdinalIgnoreCase);
string.IsNullOrWhiteSpace(name);





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
string[] collection = namesAgain.Split(';', StringSplitOptions.TrimEntries | StringSplitOptions.RemoveEmptyEntries);

foreach(string item in collection)
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
decimal cost = 1234.5m;
string cup = "Tea";

Console.WriteLine($"\n{cup, -12} £{cost, 10:N2}");