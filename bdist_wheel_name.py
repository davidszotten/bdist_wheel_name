from wheel.bdist_wheel import bdist_wheel


class bdist_wheel_name(bdist_wheel):
    def run(self):
        pass
        impl_tag, abi_tag, plat_tag = self.get_tag()
        archive_basename = "{}-{}-{}-{}".format(
            self.wheel_dist_name, impl_tag, abi_tag, plat_tag
        )
        print(archive_basename)
