#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <ctime>
using namespace std;

int main()
{
  cout << "************* Chat Bot ***************";
  while (1)
  {
    cout << "\n>>>";
    srand(time(0));
    int z;
    z = 1 + (rand() % 7);
    char s[50];
    gets(s);
   

    if (!strcmp(s, "hi") || !strcmp(s, "hii") || !strcmp(s, "hello") || !strcmp(s, "hello there") || !strcmp(s, "hy") || !strcmp(s, "yo") || !strcmp(s, "hey"))
    {
      switch (z)
      {
      case 1:
        cout << "hi there";
        break;
      case 2:
        cout << "hello there";
        break;
      case 3:
        cout << "hi";
        break;
      case 4:
        cout << "hello";
        break;
      case 5:
        cout << "hy";
        break;
      case 6:
        cout << "hey";
        break;
      case 7:
        cout << "hii";
        break;
      }
    }
    else if (!strcmp(s, "howdy?") || !strcmp(s, "howdy") || !strcmp(s, "how are you?") || !strcmp(s, "whatsup?") || !strcmp(s, "whats up?") || !strcmp(s, "how do you do?") || !strcmp(s, "how do you do") ||!strcmp(s, "how are you"))
    {
      switch (z)
      {
      case 1:
        cout << "I am fine";
        break;
      case 2:
        cout << "I am well";
        break;
      case 3:
        cout << "I am good";
        break;
      case 4:
        cout << "I am very good";
        break;
      case 5:
        cout << "fine";
        break;
      case 6:
        cout << "good";
        break;
      case 7:
        cout << "well";
        break;
      }
    }
    else if (!strcmp(s, "who are you?") || !strcmp(s, "who are you") || !strcmp(s, "who") || !strcmp(s, "who?") || !strcmp(s, "who are?") || !strcmp(s, "who are"))
    {
      switch (z)
      {
      case 1:
        cout << "I am chat bot.";
        break;
      case 2:
        cout << "I am AI machine.";
        break;
      case 3:
        cout << "I am not human. I am chat bot machine.";
        break;
      case 4:
        cout << "chat bot.";
        break;
      case 5:
        cout << "AI bot";
        break;
      case 6:
        cout << "Bot";
        break;
      case 7:
        cout << "I am computer program talking with you.";
        break;
      }
    }
    else if (!strcmp(s, "") || !strcmp(s, " ") || !strcmp(s, "  "))
    {
      switch (z)
      {
      case 1:
        cout << "why are you so silent?.";
        break;
      case 2:
        cout << "say something.";
        break;
      case 3:
        cout << "come on. talk";
        break;
      case 4:
        cout << "Stop sending blank texts";
        break;
      case 5:
        cout << "are you here to talk or what?";
        break;
      case 6:
        cout << "blank texts? seriously?";
        break;
      case 7:
        cout << "Dude. I know a blank text when I see one";
        break;
      }
    }
    else if (!strcmp(s, "bye") || !strcmp(s, "good bye") || !strcmp(s, "Bye") || !strcmp(s, "exit") || !strcmp(s, "stop"))
    {
      switch (z)
      {
      case 1:
        cout << "Sorry to say you go...";
        break;
      case 2:
        cout << "Good Bye!";
        break;
      case 3:
        cout << "Bye...!";
        break;
      case 4:
        cout << "See you lather. Bye!";
        break;
      case 5:
        cout << "Thanks for taking. Bye!";
        break;
      case 6:
        cout << "See you again...";
        break;
      case 7:
        cout << "Bye Bye";
        break;
      }
      return 0;
    }
    else {
        cout<<"You entered wrong input! Try again...";
    }

  }

     return 0;
}
