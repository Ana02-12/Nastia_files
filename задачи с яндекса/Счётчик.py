def main():
    m = int(input()) #наибол
    a = int(input()) #изнач
    b = int(input()) #цель

    if a > b:
        return (m - a) + b
    else:
        return b - a


if __name__ == '__main__':
    main()