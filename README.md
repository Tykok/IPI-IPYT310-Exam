This project was completed in a 7-hour Python exam, at the IPI School.

The objective of this exam is as follows:

1. Make a suisse tournament with a JSON file
2. Make a simple brute force program


# Suisse tournament

To run program of "Suisse tournament", just type this command in th terminal :

```shell
python main.py --suisse
```

The function will be :
1. Load the basics JSON file
2. Sort the array according to the elo points
3. Save the JSON of each opponents into a JSON file

> The JSON is loaded and casted into a `Player` class.

# Brute force

To run the "Brute force" program, just start to type :

```shell
python main.py --bruteforce=<option>
````

Here, you can understand all option value given to `bruteforce` parameter.

> All others parameters are optional, a default value is given if you don't defined the value.

## `passgen`

`passgen` value is given when you want to generate a random password of `x` characters.

With this option, you can give an other parameter will be take an int. This parameter is `--length`, with it you can specify the length of your random password.

```shell
python main.py --bruteforce=passgen --length=10
````

> By default, the length is fixed to 7

## `possibility`

`possibility` is given when you want to calculate the sum of suit for a password given.

> By default, the password is `[6Yhum`.

If you want, you can give a password with the `--password` option. Here is an example :

```shell
python main.py --bruteforce=possibility --password=AAAAAAAAAA
````

## `time`

`time` is used when you want calculate the time spend by the brute force program to retrieve your password.

You can give your password with the `--password` parameter.
Here is an example :

```shell
python main.py --bruteforce=time --password=ABCDE
````

> By default, the password is `[6Yhum`.

## `average`

`time` is used when you want calculate the time spend by the brute force program to retrieve your password.


You can give your password with the `--password` parameter, and the `--test` parameter to specify how many test will be executed.

Here is an example :

```shell
python main.py --bruteforce=average --password=ABCDE --test=10
````

> By default, the password is `[6Yhum`, and `test` parameters is equal to 10.