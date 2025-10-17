def run_this_time(every):
	from pathlib import Path

	lookfor="/tmp/{}.skip".format(Path(__file__).name)

	if Path(lookfor).exists():
		txt=Path(lookfor).read_text()
		daysago=int(txt)
		if daysago >= every - 1:
			# if daysago = 1 and args.every = 2 then delete the file and return true
			Path(lookfor).unlink()
			return True
		else:
			# increment daysago and write back
			daysago += 1
			Path(lookfor).write_text(str(daysago))
	else:
		Path(lookfor).write_text("1")

	return False

