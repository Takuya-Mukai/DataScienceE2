{
  description = "Project using your dataAnalysis devShell";
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    myOverlay.url = "github:takuya-Mukai/nix-overlay";
  };

  outputs =
    {
      self,
      nixpkgs,
      myOverlay,
    }:
    let
      system = "x86_64-linux";
    in
    {
      devShells.${system}.default = myOverlay.devShells.${system}.dataAnalysis;
    };
}
