from pytube import YouTube

while True:
    link = input("link : ").strip()
    vid = YouTube(link)
    print(f"video title: {vid.title}")

    for stream in vid.streams.filter(progressive=True):
        print(stream)
    res = input("enter resolution: \n360p, 480p, 720p or audio: ").strip().lower()
    res_list = ["360p", "480p", "720p", "audio"]
    name = print(f"{vid.title}" + f" {res}")
    try:
        while res_list.index(f"{res}") < len(res_list):
            if res == "audio":
                vid.streams.filter(mime_type="audio/mp4", type="audio", abr="128kbps", progressive=False).first().download(
                    output_path="D:/downloaded/")
                def finish():
                    print("download 100% done")
                vid.register_on_complete_callback(finish())
                break

            else:
                try:
                    vid.streams.filter(mime_type="video/mp4", type="video", res=f"{res}", progressive=True).first().download(
                    output_path="D:/downloaded/",filename=name)
                    def finish():
                        print("download 100% done")
                    vid.register_on_complete_callback(finish())
                    break

                except:
                    print("enter another resolution, this one's not available\n")
                    break

    except:
        print("enter a valid resolution\n")
    continue



